import os
from os import path
from os.path import expanduser
from configparser import ConfigParser
from cli import CLI

class Config:
    _config = ConfigParser()
    _home_dir = expanduser("~")
    _config_dir = _home_dir + "/.mp_control"
    _cli = CLI()

    def _check_config(self):
        return path.exists(self._config_dir)

    def create_configs(self):
        os.mkdir(self._config_dir)
        with open(self._config_dir + "/config", "w"): pass

        self._cli.out("Enter the name of project: ", end='')
        project_name = self._cli.get_command()

        self._cli.out("Enter the name of project directory (the directory shoult exist in the home directory): ", end='')
        project_dir = self._cli.get_command()

        self._cli.out("Enter the link to the BuildTools.jar (example https://example.com/BuildTools.jar): ", end='')
        build_tool_link = self._cli.get_command()

        self._config["PROJECT_INFO"] = {
            "name": project_name,
            "dir": self._home_dir + "/" + project_dir,
            "build_tool_link": build_tool_link
        }

        with open(self._config_dir + "/config", "w") as conf:
            self._config.write(conf)

    def get_project_name(self):
        return self._config["PROJECT_INFO"]["name"]

    def get_project_dir(self):
        return self._config["PROJECT_INFO"]["dir"]

    def get_link_to_buildtool(self):
        return self._config["PROJECT_INFO"]["build_tool_link"]

    def init(self, cli):
        self._cli = cli
        if not self._check_config():
            self.create_configs()
            self._cli.out("Configs have been created in " + self._config_dir + " directory")

        self._config.read(self._config_dir + "/config")
        self._cli.set_history_path(self._config_dir)
