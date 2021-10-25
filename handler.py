from socket_manager import SocketManager
from request_builder import RequestBuilder
from exceptions import Exit
from colored import (
    GREEN as GRN,
    YELLOW as YLW,
    BLUE as BL,
    DEFAULT as DFLT
)


class Handler:
    def __init__(self,
                 request_builder: RequestBuilder,
                 sock_manager: SocketManager) -> None:
        self.request_builder = request_builder
        self.sock_manager = sock_manager

    def handle(self, args: list[str]):
        request = self.request_builder.build(
            items=args,
            tokens=self.sock_manager.tokens)
        self.sock_manager.send(request)


class HelpHandler:
    def handle(self, *args) -> None:
        help_message = f"{GRN}To start using the chat,"
        help_message += f" you need to register and log in.\n"
        help_message += "To do this, use the following commands: \n"
        help_message += f"{YLW}/register {BL}<nickname> <password> \n"
        help_message += f"{YLW}/login {BL}<nickname> <password>\n{DFLT}\n"
        help_message += f"\n{GRN}Another commands:\n"
        help_message += f"{YLW}/help --> {GRN}Show this message\n"
        help_message += f"{YLW}/exit --> {GRN}Close session\n"

        print(help_message)


class ExitHandler:
    def handle(self, *args) -> None:
        raise Exit()
