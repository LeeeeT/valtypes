from dataclasses import dataclass
from typing import Generic, TypeVar

from valtypes.typing import SupportsReachComparison

from . import generic

__all__ = ["Base", "ExclusiveMaximum", "ExclusiveMinimum", "Maximum", "Minimum"]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class Maximum(Base, Generic[T_contra]):
    maximum: SupportsReachComparison[T_contra]
    got: SupportsReachComparison[T_contra]

    def __str__(self) -> str:
        return f"the value must be less than or equal to {self.maximum}, got: {self.got}"


@dataclass(repr=False, frozen=True)
class Minimum(Base, Generic[T_contra]):
    minimum: SupportsReachComparison[T_contra]
    got: SupportsReachComparison[T_contra]

    def __str__(self) -> str:
        return f"the value must be greater than or equal to {self.minimum}, got: {self.got}"


@dataclass(repr=False, frozen=True)
class ExclusiveMaximum(Base, Generic[T_contra]):
    exclusive_maximum: SupportsReachComparison[T_contra]
    got: SupportsReachComparison[T_contra]

    def __str__(self) -> str:
        return f"the value must be less than {self.exclusive_maximum}, got: {self.got}"


@dataclass(repr=False, frozen=True)
class ExclusiveMinimum(Base, Generic[T_contra]):
    exclusive_minimum: SupportsReachComparison[T_contra]
    got: SupportsReachComparison[T_contra]

    def __str__(self) -> str:
        return f"the value must be greater than {self.exclusive_minimum}, got: {self.got}"
