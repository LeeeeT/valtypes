from dataclasses import dataclass

from .generic import Base

__all__ = ["WrongItem", "WrongItemsCount"]


@dataclass
class WrongItem(Base):
    index: int
    cause: Base

    def __str__(self) -> str:
        return f"[{self.index}]: {self.cause}"


@dataclass
class WrongItemsCount(Base):
    expected: int
    actual: int

    def __str__(self) -> str:
        return f"{self.expected} item(s) expected, got {self.actual}"
