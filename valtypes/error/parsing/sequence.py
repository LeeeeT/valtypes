from dataclasses import dataclass

from valtypes.error import base

__all__ = ["WrongItem", "WrongItemsCount"]


@dataclass
class WrongItem(base.Base):
    index: int
    cause: base.Base

    def __str__(self) -> str:
        return f"[{self.index}]: {self.cause}"


@dataclass
class WrongItemsCount(base.Base):
    expected: int
    actual: int

    def __str__(self) -> str:
        return f"{self.expected} item(s) expected, but got {self.actual}"
