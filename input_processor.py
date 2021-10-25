from input_reader import InputReader
from command_parser import CommandParser
from router import Router
from colored import RED, GREEN
from exceptions import BadInput


class InputProcessor:
    def __init__(self,
                 input_reader: InputReader,
                 command_parser: CommandParser,
                 router: Router) -> None:
        self.input_reader = input_reader
        self.command_parser = command_parser
        self.router = router
        self.is_first_start = True

    def start(self):
        while True:
            try:
                self.help_message()
                user_input: str = self.input_reader.read()
                parsed: dict = self.command_parser.parse(user_input)
                self.router.route(parsed)
            except BadInput as err:
                print(RED, format(err), GREEN)
                self.help_message(required=True)

    def help_message(self, required=None):
        if self.is_first_start or required:
            self.router.route({"command": "/help", "args": []})
            self.is_first_start = False
