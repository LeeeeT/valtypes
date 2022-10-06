from dataclasses import dataclass

from valtypes.error import base
from valtypes.util import pretty_type_repr

__all__ = ["Composite", "NoParser", "Parsing", "Recursion", "WrongType"]


@dataclass
class NoParser(base.Base):
    type: object

    def __str__(self) -> str:
        return f"there's no parser for {pretty_type_repr(self.type)}"


@dataclass
class Recursion(base.Base):
    chain: tuple[object, ...]

    def __str__(self) -> str:
        return "recursion detected: " + " › ".join(map(pretty_type_repr, self.chain))


@dataclass
class Parsing(base.Base):
    source: object

    def __str__(self) -> str:
        return f"can't parse the value {self.source!r}"


@dataclass
class Composite(base.Base):
    causes: tuple[base.Base, ...]

    def __str__(self) -> str:
        result = "composite error"
        *others, last = map(str, self.causes)
        for other in others:
            result += "\n├ " + other.replace("\n", "\n│ ")
        result += "\n╰ " + last.replace("\n", "\n  ")
        return result


@dataclass
class WrongType(base.Base):
    source: object
    expected_type: object

    def __str__(self) -> str:
        return f"not an instance of {pretty_type_repr(self.expected_type)}"
