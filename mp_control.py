#!/usr/bin/python3

import os
from os import path
from os.path import expanduser
from configparser import ConfigParser

config_object = ConfigParser()
home_dir = expanduser("~")
config_dir = home_dir + "/.mp_control"

def check_configs():
    return path.exists(config_dir)

def create_configs(c):
    os.mkdir(config_dir)
    with open(config_dir + "/config", "w"): pass

    print("Enter the name of project: ")
    project_name = input()

    print("Enter the name of project directory (the directory shoult exist in the home directory): ")
    project_dir = input()

    print("Enter the link to the BuildTools.jar (example https://example.com/BuildTools.jar): ")
    build_tool_link = input()

    c["PROJECT_INFO"] = {
        "name": project_name,
        "dir": home_dir + "/" + project_dir,
        "build_tool_link": build_tool_link
    }

    with open(config_dir + "/config", "w") as conf:
        c.write(conf)

def download_build_tool(c):
    build_tool_dir = c["PROJECT_INFO"]["dir"] + "/build"
    if path.exists(build_tool_dir):
        print("Directory for the build tool already exists. Remove it? [y,n]: ", end='')
        command = input()
        if command == 'y':
            os.system("rm -rf " + build_tool_dir)
            print("Build tool directory has been removed!")
        else:
            return
	
    os.mkdir(build_tool_dir)
    status = os.system("wget -P " + build_tool_dir + " " + c["PROJECT_INFO"]["build_tool_link"])
    if status != 0:
        print("Failed to donwload BuildTools.jar!")
    else:
        print("BuildTools.jar has been downloaded into the " + build_tool_dir + " directory")

def build_minecraft_spigot(c):
    print("Enter the needed minecraft version: ", end='')
    version = input()
    build_tool_dir = c["PROJECT_INFO"]["dir"] + "/build"
    spigot_dir = c["PROJECT_INFO"]["dir"] + "/spigot"
    if not path.exists(build_tool_dir):
        print("BuildTools.jar not found! Cound it be downloaded? [y,n]: ", end='')
        command = input()
        if command == 'y':
            download_build_tool(c)
        else:
            return

    if not path.exists(spigot_dir):
        os.mkdir(spigot_dir)
    
    os.system("cd " + build_tool_dir + "; java -jar BuildTools.jar --rev " + version + "; cd -")
    os.system("cp " + build_tool_dir + "/spigot-" + version + ".jar " + spigot_dir)

print("MP Minecraft control panel starting...")
if not check_configs():
    create_configs(config_object)
    print("Configs have been created in " + config_dir + " directory")

config_object.read(config_dir + "/config")
if not path.exists(config_object["PROJECT_INFO"]["dir"]):
    os.mkdir(config_object["PROJECT_INFO"]["dir"])

print("Enter the command (for example \"help\")")
while 1:
    print(" > ", end='')
    command = input()
    message = ""
    
    if command == "help":
        message = "\thelp\t- list of commands\n" \
                  "\tclear\t- clear the screen\n" \
                  "\texit\t- exit from the panel\n" \
                  "\tbuildtool-download\t- donwload build tool to build spigot\n" \
                  "\tbuild-spigot\t- build the spigot server"
        print(message)
    elif command == "clear":
        os.system("clear")
    elif command == "exit":
        exit()
    elif command == "buildtool-donwload":
        download_build_tool(config_object)
    elif command == "build-spigot":
        build_minecraft_spigot(config_object)
    else:
        print("Command not found")
