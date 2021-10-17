from input_parser import InputParser
from router import Router


class InputReader:
    def __init__(self,
                 input_parser: InputParser,
                 router: Router) -> None:
        self.input_parser: InputParser = input_parser

    def input(self) -> str:
        empty_input = True
        while empty_input:
            user_input = input()  # Todo: make pretty output
            if len(user_input) != 0:
                return user_input

    def read(self) -> dict:
        user_input: str = self.input()
        request: dict = self.input_parser.parse(user_input)
        return request
