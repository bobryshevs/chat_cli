

class Router:
    def __init__(self) -> None:
        self.route_rules: dict = {}

    def register_handler(self, route_str: str, handler_func_pointer) -> None:
        self.route_rules[route_str] = handler_func_pointer

    def route(self, request: dict) -> dict:
        if request["type"] not in self.route_rules:
            return {"info": f"incorrect request type: {request['type']}"}

        return self.route_rules[request["type"]](request)
