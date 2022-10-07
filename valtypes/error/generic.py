from dataclasses import dataclass

from valtypes.util import pretty_type_repr

__all__ = ["Base", "NoParser"]


class Base(Exception):
    pass


@dataclass
class NoParser(Base, TypeError):
    type: object

    def __str__(self) -> str:
        return f"there's no parser for {pretty_type_repr(self.type)}"
