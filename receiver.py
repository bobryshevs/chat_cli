from socket_manager import SocketManager


class Receiver:
    def __init__(self, socket_manager: SocketManager) -> None:
        self.socket_manager: SocketManager = socket_manager

    def receive(self) -> bytes:
        return self.socket_manager.recv()
