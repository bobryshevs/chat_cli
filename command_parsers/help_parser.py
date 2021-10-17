from .command_parser import CommandParser


class HelpParser(CommandParser):

    def parse(self, user_input: str) -> tuple[str, dict]:
        help_message = \
            "To start using the chat, you need to register and log in.\n" \
            "To do this, use the following commands: \n" \
            "/register <nickname> <password> \n" \
            "/login <nickname> <password> \n"

        help_info = {"type": "help", "info": help_message}

        return self.command, help_info
