from exceptions import BadInput


class Router:
    def __init__(self) -> None:
        self.route_rules: dict = {}

    def register_route(self, command: str, handle_func_ptr) -> None:
        self.route_rules[command] = handle_func_ptr

    def route(self, parsed_input: dict) -> dict:
        if parsed_input["command"] not in self.route_rules:
            raise BadInput("No command with given name.")

        return self.route_rules[parsed_input["command"]](parsed_input["args"])
