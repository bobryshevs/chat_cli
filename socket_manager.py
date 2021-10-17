from socket import (
    socket,
    AF_INET,
    SOCK_STREAM,
    SOL_SOCKET,
    SO_REUSEADDR
)


class SocketManager:
    def __init__(self, server_host: str, server_port: int) -> None:
        self.__user_socket = self.create_user_socket(server_host, server_port)

    def send(self, data: bytes) -> None:
        self.__user_socket.sendall(data)

    def recv(self, buff_size: int = 1024) -> bytes:
        return self.__user_socket.recv(buff_size)

    def close_connection(self) -> None:
        self.__user_socket.close()

    def create_user_socket(self, server_host: str, server_port: int) -> socket:
        user_socket = socket(AF_INET, SOCK_STREAM)
        user_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        user_socket.connect((server_host, server_port))
        return user_socket
