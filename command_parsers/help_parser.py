from colorama.initialise import init
from .command_parser import CommandParser
from colored import (
    BLUE,
    GREEN,
    YELLOW,
    DEFAULT
)


class HelpParser(CommandParser):

    def parse(self, user_input: str) -> dict:
        help_message = \
            f"{GREEN}To start using the chat," \
            f" you need to register and log in.\n" \
            "To do this, use the following commands: \n" \
            f"{YELLOW}/register {BLUE}<nickname> <password> \n" \
            f"{YELLOW}/login {BLUE}<nickname> <password> \n{DEFAULT}\n" \
            f"\n{GREEN}Another commands:\n"\
            f"{YELLOW}/help --> {GREEN}Show this message\n" \
            f"{YELLOW}/exit --> {GREEN}Close session\n" \


        help_info = {"type": "/help", "info": help_message}

        return help_info
