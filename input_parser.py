from command_parsers import CommandParser


class InputParser:
    def __init__(self, command_parsers: list[CommandParser]) -> None:
        self.command_parsers: list[CommandParser] = command_parsers

    def parse(self, user_input: str) -> list[str]:
        for command_parser in self.command_parsers:
            if not user_input.startswith(command_parser.command):
                continue
            return command_parser.parse(user_input)


# commands
# /help
# /register nickname password
# /login nickname password
# /get_page page page_size
