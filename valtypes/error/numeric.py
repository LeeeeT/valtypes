from dataclasses import dataclass
from typing import Generic, TypeVar

from . import base

__all__ = ["Interval", "Maximum", "Minimum"]


T = TypeVar("T")


class Interval(base.Base):
    pass


@dataclass
class Maximum(Interval, Generic[T]):
    maximum: T
    got: T

    def __str__(self) -> str:
        return f"the value must be less than or equal to {self.maximum}, got: {self.got}"


@dataclass
class Minimum(Interval, Generic[T]):
    minimum: T
    got: T

    def __str__(self) -> str:
        return f"the value must be greater than or equal to {self.minimum}, got: {self.got}"
