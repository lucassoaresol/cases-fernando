from redis import Redis


class Redis:
    def __init__(self) -> None:
        self.r = Redis(host="localhost", port=6379, decode_responses=True)
