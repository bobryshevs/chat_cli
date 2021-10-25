import json


class RequestBuilder:
    def __init__(self,
                 request_type: str,
                 keys: list[str],
                 ) -> None:
        self.request_type = request_type
        self.keys = keys

    def build(self, items: list[str], tokens: dict) -> bytes:
        request: dict = self.create_dict(self.keys, items)
        request["type"] = self.request_type
        if "access" in tokens:
            request["access_token"] = tokens["access"]
        return json.dumps(request).encode("utf8")

    def create_dict(self, keys, items) -> dict:
        return {
            keys[i]: items[i]
            for i in range(
                min(len(keys), len(items))
            )
        }
