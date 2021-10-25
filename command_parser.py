

class CommandParser:

    def parse(self, user_input: str) -> dict:
        user_input = user_input.strip()
        words = user_input.split(" ")

        result = {"command": "", "args": []}
        if words[0].startswith("/"):
            result["command"] = words[0]
            words = words[1:]
        else:
            result["command"] = "/send_message"
            words = ' '.join(words)
        result["args"] = [words] if not isinstance(words, list) else words

        return result
# commands
# /help
# /register nickname password
# /login nickname password
# /get_page page page_size
