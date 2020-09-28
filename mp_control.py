#!/usr/bin/python3

import os
from os import path
from config import Config
from server import Server
from buildtools import BuildTools
from command import Command

def help():
    message = "\thelp\t\t\t- list of commands\n" \
              "\tclear\t\t\t- clear the screen\n" \
              "\texit\t\t\t- exit from the panel\n" \
              "\tdownload-buildtool\t- donwload build tool to build spigot\n" \
              "\tbuild-spigot\t\t- build the spigot server\n" \
              "\tavailable-versions\t- get list of available minecraft versions\n" \
              "\tcreate-server\t\t- create minecraft server\n" \
              "\thistory\t\t\t- history of writted commands"
    print(message)

print("MP Minecraft control panel starting...")
command_c = Command()
config_object = Config()
config_object.init(command_c)
if not path.exists(config_object.get_project_dir()):
    os.mkdir(config_object.get_project_dir())

build_tools = BuildTools(config_object, command_c)
server = Server(config_object, command_c)

print("Enter the command (for example \"help\")")
while 1:
    print(" > ", end='')
    command = command_c.write()
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
        command_c.history()
    else:
        print("Command not found")
