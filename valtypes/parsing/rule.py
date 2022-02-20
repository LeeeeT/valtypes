from . import parser

__all__ = ["Rule"]


class Rule:
    def __init__(self, parser: parser.ABC, /, *, source_type: object = object, target_type: object = object):
        self.parser = parser
        self.source_type = source_type
        self.target_type = target_type
