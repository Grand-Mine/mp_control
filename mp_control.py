#!/usr/bin/python3

import os
from config import Config
from os import path

def help():
    message = "\thelp\t\t\t- list of commands\n" \
              "\tclear\t\t\t- clear the screen\n" \
              "\texit\t\t\t- exit from the panel\n" \
              "\tdownload-buildtool\t- donwload build tool to build spigot\n" \
              "\tbuild-spigot\t\t- build the spigot server\n" \
              "\tavailable-versions\t- get list of available minecraft versions\n" \
              "\tcreate-server\t\t- create minecraft server"
    print(message)

def download_build_tool(c):
    build_tool_dir = c.get_project_dir() + "/build"
    build_tool_link = c.get_link_to_buildtool()
    if path.exists(build_tool_dir):
        print("Directory for the build tool already exists. Remove it? [y,n]: ", end='')
        command = input()
        if command == 'y':
            os.system("rm -rf " + build_tool_dir)
            print("Build tool directory has been removed!")
        else:
            return

    os.mkdir(build_tool_dir)
    status = os.system("wget -P " + build_tool_dir + " " + build_tool_link)
    if status != 0:
        print("Failed to donwload BuildTools.jar!")
    else:
        print("BuildTools.jar has been downloaded into the " + build_tool_dir + " directory")

def build_minecraft_spigot(c, _version="Not Defined"):
    version = str()
    if _version == "Not Defined":
        print("Enter the needed minecraft version: ", end='')
        version = input()
    else:
        version = _version

    build_tool_dir = c.get_project_dir() + "/build"
    spigot_dir = c.get_project_dir() + "/spigot"
    if not path.exists(build_tool_dir):
        print("BuildTools.jar not found! Cound it be downloaded? [y,n]: ", end='')
        command = input()
        if command == 'y':
            download_build_tool(c)
        else:
            return -1

    if not path.exists(spigot_dir):
        os.mkdir(spigot_dir)
    
    status = os.system("cd " + build_tool_dir + "; java -jar BuildTools.jar --rev " + version + "; cd -")
    
    if not path.exists(build_tool_dir + "/spigot-" + version + ".jar"):
        print("Error of building spigot " + version)
        return -1
    os.system("cp " + build_tool_dir + "/spigot-" + version + ".jar " + spigot_dir)

    return 0

def get_list_of_available_versions(c):
    spigot_dir = c.get_project_dir() + "/spigot"
    versions = os.listdir(spigot_dir)
    for i in range(len(versions)):
        versions[i] = versions[i].replace("spigot-", "")
        versions[i] = versions[i].replace(".jar", "")
    
    print("Available minecraft versions: " + " ".join(versions))

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
            status = build_minecraft_spigot(c, server_version)
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
if not path.exists(config_object.get_project_dir()):
    os.mkdir(config_object.get_project_dir())

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
        download_build_tool(config_object)
    elif command == "build-spigot":
        build_minecraft_spigot(config_object)
    elif command == "available-versions":
        get_list_of_available_versions(config_object)
    elif command == "create-server":
        create_server(config_object)
    else:
        print("Command not found")
