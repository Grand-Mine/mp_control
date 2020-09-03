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

    c["PROJECT_INFO"] = {
        "name": project_name,
        "dir": home_dir + "/" + project_dir
    }

    with open(config_dir + "/config", "w") as conf:
        c.write(conf)


print("MP Minecraft control panel starting...")
if not check_configs():
    create_configs(config_object)
    print("Configs have been created in " + config_dir + " directory")

config_object.read(config_dir + "/config")
