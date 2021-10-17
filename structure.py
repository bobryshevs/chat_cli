from dotenv import dotenv_values

from command_parsers import (
    HelpParser,
    LoginParser,
    RegisterParser
)
from handlers import (
    HelpHandler
)
from socket_manager import SocketManager
from router import Router
from input_reader import InputReader
from input_parser import InputParser
from receiver import Receiver
from app import App

config = dotenv_values(".env")

socket_manager = SocketManager(
    server_host=config["SERVER_HOST"],
    server_port=int(config["SERVER_PORT"])
)
# --- Command parsers --- #
help_command_parser = HelpParser(command="/help", args_count=0)
login_command_parser = LoginParser(command="/login ", args_count=2)
register_command_parser = RegisterParser(command="/register ", args_count=2)


receiver = Receiver(socket_manager=socket_manager)
input_parser = InputParser(
    [
        help_command_parser,
        login_command_parser,
        register_command_parser
    ]
)

# --- Handlers --- #
help_handler = HelpHandler(socket_manager)


# --- Roueter config
router = Router()
router.register_handler(
    route_str="/help",
    handler_func_pointer=help_handler.handle
)


input_reader = InputReader(
    input_parser=input_parser,
    router=router
)


app = App(
    input_reader=input_reader,
    receiver=receiver
)
