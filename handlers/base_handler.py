from abc import abstractmethod

from socket_manager import SocketManager


class BaseHandler:
    def __init__(self, socket_manager: SocketManager) -> None:
        self.socket_manager: SocketManager = socket_manager

    @abstractmethod
    def handle(self, request: dict) -> str: ...
