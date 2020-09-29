import os
from os import path
from cli import CLI
from config import Config

class BuildTools:
    _config = Config()
    _cli = CLI()

    def __init__(self, config, cli):
        self._config = config
        self._cli = cli

    def download(self):
        build_tool_dir = self._config.get_project_dir() + "/build"
        build_tool_link = self._config.get_link_to_buildtool()
        if path.exists(build_tool_dir):
            self._cli.out("Directory for the build tool already exists. Remove it? [y,n]: ", end='')
            command = input()
            if command == 'y':
                os.system("rm -rf " + build_tool_dir)
                self._cli.out("Build tool directory has been removed!")
            else:
                return

        os.mkdir(build_tool_dir)
        status = os.system("wget -P " + build_tool_dir + " " + build_tool_link)
        if status != 0:
            self._cli.out("Failed to donwload BuildTools.jar!")
        else:
            self._cli.out("BuildTools.jar has been downloaded into the " + build_tool_dir + " directory")

    def build(self, _version="Not Defined"):
        version = str()
        if _version == "Not Defined":
            self._cli.out("Enter the needed minecraft version: ", end='')
            version = input()
        else:
            version = _version

        build_tool_dir = self._config.get_project_dir() + "/build"
        spigot_dir = self._config.get_project_dir() + "/spigot"
        if not path.exists(build_tool_dir):
            self._cli.out("BuildTools.jar not found! Cound it be downloaded? [y,n]: ", end='')
            command = input()
            if command == 'y':
                self.download()
            else:
                return -1

        if not path.exists(spigot_dir):
            os.mkdir(spigot_dir)
    
        status = os.system("cd " + build_tool_dir + "; java -jar BuildTools.jar --rev " + version + "; cd -")
    
        if not path.exists(build_tool_dir + "/spigot-" + version + ".jar"):
            self._cli.out("Error of building spigot " + version)
            return -1
        os.system("cp " + build_tool_dir + "/spigot-" + version + ".jar " + spigot_dir)

        return 0

    def get_versions(self):
        spigot_dir = self._config.get_project_dir() + "/spigot"
        try:
            versions = os.listdir(spigot_dir)
        except IOError:
            versions = [""]

        for i in range(len(versions)):
            versions[i] = versions[i].replace("spigot-", "")
            versions[i] = versions[i].replace(".jar", "")
    
        self._cli.out("Available minecraft versions: " + " ".join(versions))

