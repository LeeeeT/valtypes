from dataclasses import dataclass
from typing import TypeVar

from . import generic

__all__ = ["Base", "ExclusiveMaximum", "ExclusiveMinimum", "Maximum", "Minimum"]


T = TypeVar("T")


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class Maximum(Base):
    maximum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be less than or equal to {self.maximum}, got: {self.got}"


@dataclass(repr=False, frozen=True)
class Minimum(Base):
    minimum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be greater than or equal to {self.minimum}, got: {self.got}"


@dataclass(repr=False, frozen=True)
class ExclusiveMaximum(Base):
    exclusive_maximum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be less than {self.exclusive_maximum}, got: {self.got}"


@dataclass(repr=False, frozen=True)
class ExclusiveMinimum(Base):
    exclusive_minimum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be greater than {self.exclusive_minimum}, got: {self.got}"
