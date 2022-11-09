from collections.abc import Sequence
from dataclasses import dataclass
from typing import Self

from valtypes.error import generic
from valtypes.util import type_repr

__all__ = ["Base", "Union", "WrongType"]


class Base(generic.Base, ValueError):
    pass


@dataclass(repr=False, frozen=True)
class WrongType(Base):
    expected_type: object
    got: object

    def __str__(self) -> str:
        return f"not an instance of {type_repr(self.expected_type)}"


@dataclass(repr=False, frozen=True)
class Union(ExceptionGroup[Base], Base):
    errors: Sequence[Base]
    got: object

    def __new__(cls, errors: Sequence[Base], got: object) -> Self:
        return super().__new__(cls, "union parsing error", errors)

    def derive(self, errors: Sequence[Base]) -> Self:
        return self.__class__(errors, self.got)
