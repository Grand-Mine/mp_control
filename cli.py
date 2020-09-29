import sys
import threading
from os import path
from os.path import expanduser
from getkey import getkey, keys

class CLI:
    _max_history_size = 1000
    _history = []
    _history_path = expanduser("~") + "/history"

    def read_keyboard(self):
        command = ""
        while(True):
            key = getkey(blocking=True)
            if key == keys.ENTER:
                self.out('')
                return command
            elif key == keys.BACKSPACE:
                if len(command) == 0:
                    continue
                self.out('\b \b', end='')
                command = command[:-1]
            elif key == keys.UP:
                try:
                    command = self._history.pop()
                    self.out(command, end='')
                except Exception:
                    self.out("History is empty")
            else:
                command += key
                self.out(key, end='')
    
    def get_command(self):
        command = self.read_keyboard()
        self._history.append(command)
        if len(self._history) > 1000:
            self._history.pop(0)

        with open(self._history_path, 'w') as history_file:
            for command in self._history:
                history_file.write(command + '\n')

        return command

    def history(self):
        with open(self._history_path, 'r') as history_file:
            self.out(history_file.read())

    def set_history_path(self, history_path):
        self._history_path = history_path + "/history"
        if not path.exists(self._history_path):
            with open(self._history_path, 'w'): pass

        with open(self._history_path, 'r') as history:
            for line in history:
                self._history.append(line[:-1])

    def out(self, message, end='\n'):
        for char in message:
            sys.stdout.write(char)
        sys.stdout.write(end)
        sys.stdout.flush()
