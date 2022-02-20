__all__ = ["ParsingError", "NoParserFoundError"]


class ParsingError(ValueError):
    def __init__(self, target_type: object, value: object):
        pass


class NoParserFoundError(LookupError):
    def __init__(self, source_type: object, target_type: object):
        pass
