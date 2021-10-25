from datetime import datetime
import json
from router import Router
from socket_manager import SocketManager
from colored import (
    RED,
    YELLOW as YLW,
    BLUE as BL,
    GREEN as GRN,
    DEFAULT as DFLT
)
from exceptions import Exit


class Receiver:
    def __init__(self, socket_manager: SocketManager, router: Router) -> None:
        self.socket_manager: SocketManager = socket_manager
        self.rotuer: Router = router

    def receive(self) -> bytes:
        while True:
            try:
                raw_data: str = self.socket_manager.recv()
                response: dict = self.decode_response(raw_data)
                self.process_response(response)
            except json.JSONDecodeError as err:
                print("Bad data. Receiver doesn't work. Restart app.")
                raise Exit()

    def process_response(self, response: dict) -> None:
        response: dict = self.parse_response(response)
        if response["type"] == "error":
            self.process_error_response(response)
        elif response["type"] == "register":
            self.process_register_response(response)
        elif response["type"] == "login":
            self.process_login_response(response)
            self.rotuer.route({
                "command": "/message_page",
                "args": [1, 10]  # page, page_size
            })
        elif response["type"] == "message_page":
            self.process_message_page(response)
        elif response["type"] == "send_message":
            self.process_send_message(response)
        else:
            print(response)

    def parse_response(self, response: dict) -> dict:
        response["content"] = json.loads(response["content"].strip())
        return response

    def process_send_message(self, response: dict) -> None:
        self.show_message(response["content"])

    def process_message_page(self, response: dict) -> None:
        for message in response["content"]["items"]:
            self.show_message(message)

    def show_message(self, message: dict) -> None:
        date = datetime.fromtimestamp(message["timestamp"]).isoformat()
        author = message["author"]
        to_print = f"{GRN}[{YLW}{date}{GRN}] - {BL}{author} {RED}"
        if len(to_print) < 50:
            to_print += " " * (50 - len(to_print))
        to_print += "|" + DFLT + " "
        to_print += message["text"]
        print(to_print)

    def process_login_response(self, response: dict) -> None:
        self.socket_manager.tokens = {
            "access": response["content"]["access"],
            "refresh": response["content"]["refresh"]
        }
        print("\n" + BL + "You have logged in." + GRN)

    def process_register_response(self, response: dict) -> None:
        to_print = "\nSuccessful registered\n"
        to_print += f"Your nickname: {YLW}{response['content']['nickname']}\n"
        to_print += f"{GRN}"
        to_print += f"Your id: {YLW}{response['content']['id']}{GRN}"
        print(to_print)

    def process_error_response(self, response: dict) -> None:
        print(RED, response["content"]["msg"], GRN)

    def decode_response(self, response: bytes) -> dict:
        return json.loads(response.decode("utf8"))
