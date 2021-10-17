from .command_parser import CommandParser


class ExitParser(CommandParser):

    def parse(self, user_input: str) -> dict:
        return {"type": "/exit", "info": "stopping application"}
