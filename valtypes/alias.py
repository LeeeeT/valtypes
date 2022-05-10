__all__ = ["ALIASES_KEY", "Alias"]


ALIASES_KEY = object()


class Alias(dict[object, tuple[str, ...]]):
    def __init__(self, *aliases: str):
        super().__init__({ALIASES_KEY: aliases})
