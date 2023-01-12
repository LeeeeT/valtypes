from collections.abc import Sequence
from dataclasses import dataclass
from typing import Self

from . import generic

__all__ = ["Base", "Composite", "InvalidValue", "NotMember"]


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class Composite(ExceptionGroup[Base], Base):
    errors: Sequence[Base]
    got: object

    def __new__(cls, errors: Sequence[Base], got: object) -> Self:
        return super().__new__(cls, "literal parsing error", errors)

    def derive(self, errors: Sequence[Base]) -> Self:
        return self.__class__(errors, self.got)


@dataclass(repr=False, frozen=True)
class InvalidValue(ExceptionGroup[generic.Base], Base):
    choice: object
    cause: generic.Base
    got: object

    def __new__(cls, choice: object, cause: generic.Base, got: object) -> Self:
        return super().__new__(cls, f"can't check if the value is {choice!r}", [cause])

    def derive(self, errors: Sequence[generic.Base]) -> Self:
        return self.__class__(self.choice, errors[0], self.got)


@dataclass(repr=False, frozen=True)
class NotMember(Base):
    choice: object
    got: object

    def __str__(self) -> str:
        return f"the value is not {self.choice!r}"
