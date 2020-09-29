import os
from os import path
from cli import CLI
from config import Config
from buildtools import BuildTools

class Server:
    _config = Config()
    _cli = CLI()

    def __init__(self, config, cli):
        self._config = config
        self._cli = cli

    def create(self, build_tools):
        self._cli.out("Enter the server name: ", end='')
        server_name = self._cli.get_command()

        self._cli.out("Enter the server version: ", end='')
        server_version = self._cli.get_command()

        spigot = self._config.get_project_dir() + "/spigot/spigot-" + server_version + ".jar"
        servers_dir = self._config.get_project_dir() + "/servers"
        server_dir = servers_dir + '/' + server_name

        if not path.exists(servers_dir):
            os.mkdir(servers_dir)

        if not path.exists(spigot):
            self._cli.out("The version " + server_version + " of spigot not available! Build it? [y,n]: ", end='')
            command = self._cli.get_command()
            if command == 'y':
                status = build_tools.build(server_version)
                if status != 0:
                    self._cli.out("Error of creating server")
                    return
            else:
                return        

        if path.exists(server_dir):
            self._cli.out("The name \"" + server_name + "\" already exists!")
            return
        os.mkdir(server_dir)
        os.system("cp " + spigot + " " + server_dir)
        os.system("echo eula=true > " + server_dir + "/eula.txt")
        os.system("echo java -Xms2G -Xmx2G -XX:+UseG1GC -jar spigot-" + server_version + ".jar nogui > " + server_dir + "/wrapper.sh")
        self._cli.out("Server has been created")

    def lunch(self):
        self._cli.out("Enter the server name: ", end='')
        server_name = self._cli.get_command()
        server_dir = self._config.get_project_dir() + "/servers/" + server_name

        if not path.exists(server_dir):
            self._cli.out("Server [" + server_name + "] not found")
            return

        os.system("cd " + server_dir + "; screen -S mp_control_" + server_name)

    def stop(self):
        self._cli.out("Enter the server name: ", end='')
        server_name = self._cli.get_command()

        status = os.system("screen -S mp_control_" + server_name + " -X quit")
        if status != 0:
            self._cli.out("Failed to stop the server " + server_name)
            return

        self._cli.out("The server " + server_name + " has been stopped")

    def show(self):
        self._cli.out("Enter the server name: ", end='')
        server_name = self._cli.get_command()

        status = os.system("screen -r mp_control_" + server_name)
        if status != 0:
            self._cli.out("Failed to show the server console for the server " + server_name)
