from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Self

from . import generic

__all__ = ["Base", "Composite", "MissingField", "WrongFieldValue"]


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class Composite(ExceptionGroup[Base], generic.Base):
    errors: Sequence[Base]
    got: Mapping[str, object]

    def __new__(cls, errors: Sequence[Base], got: Mapping[str, object]) -> Self:
        return super().__new__(cls, "dataclass parsing error", errors)

    def derive(self, errors: Sequence[Base]) -> Self:
        return self.__class__(errors, self.got)


@dataclass(repr=False, frozen=True)
class WrongFieldValue(ExceptionGroup[generic.Base], Base):
    field: str
    cause: generic.Base
    got: object

    def __new__(cls, field: str, cause: generic.Base, got: object) -> Self:
        return super().__new__(cls, f"can't parse field {field!r}", [cause])

    def derive(self, errors: Sequence[generic.Base]) -> Self:
        return self.__class__(self.field, errors[0], self.got)


@dataclass(repr=False, frozen=True)
class MissingField(Base):
    field: str

    def __str__(self) -> str:
        return f"required field {self.field!r} is missing"
