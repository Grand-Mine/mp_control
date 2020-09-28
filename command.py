import threading
import keyboard

class Command:
    _max_history_size = 1000
    _history = []
    _command = str()

    def write(self):
        command = input()
        self._history.append(command)
        if len(self._history) > 1000:
            self._history.pop(0)

        self._command = command
        return command
