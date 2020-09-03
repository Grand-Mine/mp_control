#!/usr/bin/python3

import os
from os import path
from os.path import expanduser

home_dir = expanduser("~")
config_dir = home_dir + "/.mp_control"

def check_configs():
    return path.exists(config_dir)

def create_configs():
    os.mkdir(config_dir)
    with open(config_dir + "/config", "w"): pass

print("MP Minecraft control panel starting...")
if not check_configs():
    create_configs()
    print("Configs have been created in " + config_dir + " directory")
