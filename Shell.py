from Interpreter import Interpreter

class Shell:
    def __init__(self):
        self._interpreter = Interpreter()
        self._PROMPT = ">>"
        self._run()

    def _run(self):
        while True:
            line = input(self._PROMPT + " ")
            self._interpreter.interpret(line)
