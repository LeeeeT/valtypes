from dataclasses import dataclass

from . import generic

__all__ = ["Base", "MaximumLength", "MinimumLength"]


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class MaximumLength(Base):
    maximum: int
    got: int

    def __str__(self) -> str:
        return f"length {self.got} is greater than the allowed maximum of {self.maximum}"


@dataclass(repr=False, frozen=True)
class MinimumLength(Base):
    minimum: int
    got: int

    def __str__(self) -> str:
        return f"length {self.got} is less than the allowed minimum of {self.minimum}"
