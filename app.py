from threading import Thread

from input_handler import InputHandler
from input_reader import InputReader
from receiver import Receiver


class App:
    def __init__(
            self,
            input_reader: InputReader,
            input_handler: InputHandler,
            receiver: Receiver) -> None:

        self.input_reader: InputReader = input_reader
        self.input_hanlder: InputHandler = input_handler
        self.receiver: Receiver = receiver
        self.threads: list[Thread] = []
        self.receive_thread = self.get_thread(target=self.receiver.receive)

    def get_thread(self, target) -> Thread:
        thread = Thread(target=target)
        thread.daemon = True
        self.threads.append(thread)
        return thread

    def run(self):
        self.start_message()
        while True:
            if not self.receive_thread.is_alive:
                self.receive_thread.start()

            request: dict = self.input_reader.read()
            self.input_hanlder.handle(request)

    def start_message(self) -> None:
        self.input_hanlder.handle(
            self.input_reader.input_parser.parse("/help")
        )

    def close_threads(self):
        for thread in self.threads:
            thread.join()
