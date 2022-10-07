from dataclasses import dataclass
from typing import TypeVar

from valtypes.error.generic import Base

__all__ = ["ExclusiveMaximum", "ExclusiveMinimum", "Maximum", "Minimum"]


T = TypeVar("T")


@dataclass
class Maximum(Base):
    maximum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be less than or equal to {self.maximum}, got: {self.got}"


@dataclass
class Minimum(Base):
    minimum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be greater than or equal to {self.minimum}, got: {self.got}"


@dataclass
class ExclusiveMaximum(Base):
    exclusive_maximum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be less than {self.exclusive_maximum}, got: {self.got}"


@dataclass
class ExclusiveMinimum(Base):
    exclusive_minimum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be greater than {self.exclusive_minimum}, got: {self.got}"
