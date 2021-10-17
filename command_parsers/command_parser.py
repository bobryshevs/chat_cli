from abc import abstractmethod


class CommandParser:
    def __init__(self, command: str, args_count: int) -> None:
        self.command: str = command
        self.args_count: int = args_count

    @abstractmethod
    def parse(self, user_input: str) -> dict: ...
