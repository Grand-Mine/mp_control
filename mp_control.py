#!/usr/bin/python3

import os
from os import path
from config import Config
from server import Server
from buildtools import BuildTools

def help():
    message = "\thelp\t\t\t- list of commands\n" \
              "\tclear\t\t\t- clear the screen\n" \
              "\texit\t\t\t- exit from the panel\n" \
              "\tdownload-buildtool\t- donwload build tool to build spigot\n" \
              "\tbuild-spigot\t\t- build the spigot server\n" \
              "\tavailable-versions\t- get list of available minecraft versions\n" \
              "\tcreate-server\t\t- create minecraft server"
    print(message)

print("MP Minecraft control panel starting...")
config_object = Config()
config_object.init()
if not path.exists(config_object.get_project_dir()):
    os.mkdir(config_object.get_project_dir())

build_tools = BuildTools(config_object)
server = Server(config_object)

print("Enter the command (for example \"help\")")
while 1:
    print(" > ", end='')
    command = input()
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
        build_tools.versions(config_object)
    elif command == "create-server":
        server.create(build_tools)
    else:
        print("Command not found")
