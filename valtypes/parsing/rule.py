from collections.abc import Callable

from . import parser

__all__ = ["Rule"]


class Rule:
    def __init__(self, parser: parser.Proto, target_condition: Callable[[object], bool]):
        self.parser = parser
        self.target_condition = target_condition
