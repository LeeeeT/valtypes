__all__ = ["ParsingError", "NoParserFoundError"]


class ParsingError(ValueError):
    def __init__(self, target_type: object, source: object):
        pass


class NoParserFoundError(ParsingError):
    pass
