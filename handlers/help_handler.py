from .base_handler import BaseHandler


class HelpHandler(BaseHandler):

    def handle(self, request: dict) -> str:
        return request["info"]
