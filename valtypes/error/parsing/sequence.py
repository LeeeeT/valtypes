from collections.abc import Sequence
from dataclasses import dataclass
from typing import Self

from . import generic

__all__ = ["Base", "Composite", "WrongItem", "WrongItemsCount"]


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class Composite(ExceptionGroup[Base], Base):
    errors: Sequence[Base]
    got: object

    def __new__(cls, errors: Sequence[Base], got: object) -> Self:
        return super().__new__(cls, "sequence parsing error", errors)

    def derive(self, errors: Sequence[Base]) -> Self:
        return self.__class__(errors, self.got)


@dataclass(repr=False, frozen=True)
class WrongItem(ExceptionGroup[generic.Base], Base):
    index: int
    cause: generic.Base
    got: object

    def __new__(cls, index: int, cause: generic.Base, got: object) -> Self:
        return super().__new__(cls, f"can't parse item at index {index}", [cause])

    def derive(self, errors: Sequence[generic.Base]) -> Self:
        return self.__class__(self.index, errors[0], self.got)


@dataclass(repr=False, frozen=True)
class WrongItemsCount(Base):
    expected: int
    got: int

    def __str__(self) -> str:
        return f"{self.expected} item(s) expected, got {self.got}"
