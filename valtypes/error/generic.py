from dataclasses import dataclass

from valtypes.util import type_repr

__all__ = ["Base", "NoParser"]


class Base(Exception):
    pass


@dataclass(repr=False, frozen=True)
class NoParser(Base, TypeError):
    type: object

    def __str__(self) -> str:
        return f"there's no parser for {type_repr(self.type)}"
