from .command_parser import CommandParser
from exceptions import BadInput


class LoginParser(CommandParser):

    def parse(self, user_input: str) -> tuple[str, dict]:
        user_input = user_input.removeprefix(self.command)
        raw_data = user_input.split(" ")
        if len(raw_data) != self.args_count:
            raise BadInput("incorrect arguments for <login> command")
        args = {
            "type": self.command,
            "nickname": raw_data[0],
            "password": raw_data[1]
        }
        return self.command, args
