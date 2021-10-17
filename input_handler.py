from router import Router


class InputHandler:
    def __init__(self, router: Router) -> None:
        self.router: Router = router

    def handle(self, request: dict) -> None:
        print(self.router.route(request))
