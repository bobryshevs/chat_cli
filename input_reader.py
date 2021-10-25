

class InputReader:

    def read(self) -> str:
        while True:
            user_input = input()
            if user_input:
                return user_input
