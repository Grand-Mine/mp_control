import os
from os import path
from config import Config
from buildtools import BuildTools
from command import Command

class Server:
    _config = Config()
    _command = Command()

    def __init__(self, config, command):
        self._config = config
        self._command = command

    def create(self, build_tools):
        print("Enter the server name: ", end='')
        server_name = self._command.write()

        print("Enter the server version: ", end='')
        server_version = self._command.write()

        spigot = self._config.get_project_dir() + "/spigot/spigot-" + server_version + ".jar"
        servers_dir = self._config.get_project_dir() + "/servers"
        server_dir = servers_dir + '/' + server_name

        if not path.exists(servers_dir):
            os.mkdir(servers_dir)

        if not path.exists(spigot):
            print("The version " + server_version + " of spigot not available! Build it? [y,n]: ", end='')
            command = self._command.write()
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
        os.system("echo java -Xms2G -Xmx2G -XX:+UseG1GC -jar spigot-" + server_version + ".jar nogui > " + server_dir + "/wrapper.sh")
        print("Server has been created")
