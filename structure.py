from dotenv import dotenv_values
from command_parser import CommandParser
from handler import (
    Handler,
    HelpHandler,
    ExitHandler
)
from request_builder import RequestBuilder
from socket_manager import SocketManager
from router import Router
from input_reader import InputReader
from input_processor import InputProcessor
from receiver import Receiver
from app import App

config = dotenv_values(".env")

input_reader = InputReader()
command_parser = CommandParser()
router = Router()

input_processor = InputProcessor(
    input_reader=input_reader,
    command_parser=command_parser,
    router=router,
)

socket_manager = SocketManager(
    server_host=config["SERVER_HOST"],
    server_port=int(config["SERVER_PORT"])
)

receiver = Receiver(socket_manager=socket_manager, router=router)

app = App(
    input_processor=input_processor,
    receiver=receiver)

# __ RequestBuilders __ #
register_request_builder = RequestBuilder(
    request_type="register",
    keys=["nickname", "password"]
)
login_request_builder = RequestBuilder(
    request_type="login",
    keys=["nickname", "password"]
)
get_message_page_request_builder = RequestBuilder(
    request_type="message_page",
    keys=["page", "page_size", "access_token"]
)
send_message_request_builder = RequestBuilder(
    request_type="send_message",
    keys=["text", "access_token"]
)

# __ Handlers __
help_handler = HelpHandler()
exit_handler = ExitHandler()
register_handler = Handler(
    request_builder=register_request_builder,
    sock_manager=socket_manager
)
login_handler = Handler(
    request_builder=login_request_builder,
    sock_manager=socket_manager)

get_message_page_handler = Handler(
    request_builder=get_message_page_request_builder,
    sock_manager=socket_manager
)
send_message_handler = Handler(
    request_builder=send_message_request_builder,
    sock_manager=socket_manager
)
