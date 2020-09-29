#!/usr/bin/python3

import os
from os import path
from config import Config
from server import Server
from buildtools import BuildTools
from cli import CLI

def help():
    message = "\thelp\t\t\t- list of commands\n" \
              "\tclear\t\t\t- clear the screen\n" \
              "\texit\t\t\t- exit from the panel\n" \
              "\tdownload-buildtool\t- donwload build tool to build spigot\n" \
              "\tbuild-spigot\t\t- build the spigot server\n" \
              "\tavailable-versions\t- get list of available minecraft versions\n" \
              "\tcreate-server\t\t- create minecraft server\n" \
              "\thistory\t\t\t- history of writted commands\n" \
              "\tlunch\t\t\t- lunch the minecraft server\n" \
              "\tstop\t\t\t- stop the minecraft server\n" \
              "\tshow\t\t\t- show the server console\n"
    print(message, end='')

print("MP Minecraft control panel starting...")
cli = CLI()
config_object = Config()
config_object.init(cli)
if not path.exists(config_object.get_project_dir()):
    os.mkdir(config_object.get_project_dir())

build_tools = BuildTools(config_object, cli)
server = Server(config_object, cli)

print("Enter the command (for example \"help\")")
while 1:
    cli.out(" > ", end='')
    command = cli.get_command()
    message = ""
    
    if command == "help":
        help()
    elif command == "clear":
        os.system("clear")
    elif command == "exit":
        exit()
    elif command == "donwload-buildtool":
        build_tools.download()
    elif command == "build-spigot":
        build_tools.build()
    elif command == "available-versions":
        build_tools.get_versions()
    elif command == "create-server":
        server.create(build_tools)
    elif command == "history":
        cli.history()
    elif command == "lunch":
        server.lunch()
    elif command == "stop":
        server.stop()
    elif command == "show":
        server.show()
    else:
        cli.out("Command not found")
