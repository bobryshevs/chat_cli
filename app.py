from threading import Thread

from input_processor import InputProcessor
from receiver import Receiver


class App:
    def __init__(
            self,
            input_processor: InputProcessor,
            receiver: Receiver) -> None:
        self.input_processor = input_processor
        self.receiver: Receiver = receiver
        self.receive_thread = self.__get_thread(target=self.receiver.receive)
        self.receive_thread.start()

    def __get_thread(self, target) -> Thread:
        thread = Thread(target=target)
        thread.daemon = True
        return thread

    def run(self):
        # receive thread start with init
        self.input_processor.start()
