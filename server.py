import os
from os import path
from config import Config
from buildtools import BuildTools

class Server:
    _config = Config()

    def __init__(self, config):
        _config = config

    def create(self, build_tools):
        print("Enter the server name: ", end='')
        server_name = input()

        print("Enter the server version: ", end='')
        server_version = input()

        spigot = self._config.get_project_dir() + "/spigot/spigot-" + server_version + ".jar"
        servers_dir = self._config.get_project_dir() + "/servers"
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
        os.system("echo eula=true > " + server_dir + "/eula.txt")
        print("Server has been created")
