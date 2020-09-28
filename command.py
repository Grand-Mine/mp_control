import threading
import keyboard
from os.path import expanduser

class Command:
    _max_history_size = 1000
    _history = []
    _command = str()
    _history_path = expanduser("~") + "/history"

    def write(self):
        command = input()
        self._history.append(command)
        if len(self._history) > 1000:
            self._history.pop(0)

        with open(self._history_path, 'w') as history_file:
            for command in self._history:
                history_file.write(command + '\n')

        self._command = command
        return command

    def history(self):
        with open(self._history_path, 'r') as history_file:
            print(history_file.read())

    def set_history_path(self, path):
        self._history_path = path + "/history"
