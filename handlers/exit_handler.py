from .base_handler import BaseHandler
from exceptions import Exit


class ExitHandler(BaseHandler):
    def handle(self, request: dict) -> str:
        raise Exit()
