from dataclasses import dataclass

from valtypes.error import generic

__all__ = ["Base", "Composite", "WrongType"]

from valtypes.util import pretty_type_repr


class Base(generic.Base, ValueError):
    pass


@dataclass
class Composite(Base):
    causes: tuple[Base, ...]

    def __str__(self) -> str:
        result = "composite error"
        *others, last = map(str, self.causes)
        for other in others:
            result += "\n├ " + other.replace("\n", "\n│ ")
        result += "\n╰ " + last.replace("\n", "\n  ")
        return result


@dataclass
class WrongType(Base):
    source: object
    expected_type: object

    def __str__(self) -> str:
        return f"not an instance of {pretty_type_repr(self.expected_type)}"
