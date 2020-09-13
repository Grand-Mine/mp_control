#!/usr/bin/python3

import os
from os import path
from config import Config
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

def create_server(c):
    print("Enter the server name: ", end='')
    server_name = input()

    print("Enter the server version: ", end='')
    server_version = input()

    spigot = c.get_project_dir() + "/spigot/spigot-" + server_version + ".jar"
    servers_dir = c.get_project_dir() + "/servers"
    server_dir = servers_dir + '/' + server_name

    if not path.exists(servers_dir):
        os.mkdir(servers_dir)

    if not path.exists(spigot):
        print("The version " + server_version + " of spigot not available! Build it? [y,n]: ", end='')
        command = input()
        if command == 'y':
            status = build_tools.build(server_version)
            if status != 0:
                print("Error of creating server")
                return
        else:
            return        

    if path.exists(server_dir):
        print("The name \"" + server_name + "\" already exists!")
        return
    os.mkdir(server_dir)
    os.system("cp " + spigot + " " + server_dir)
    print("Server has been created")
    

print("MP Minecraft control panel starting...")
config_object = Config()
config_object.init()
if not path.exists(config_object.get_project_dir()):
    os.mkdir(config_object.get_project_dir())

build_tools = BuildTools(config_object)

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
        create_server(config_object)
    else:
        print("Command not found")
