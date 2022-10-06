from dataclasses import dataclass

from . import base

__all__ = ["MaximumLength", "MinimumLength"]


@dataclass
class MaximumLength(base.Base):
    maximum: int
    length: int

    def __str__(self) -> str:
        return f"length {self.length} is greater than the allowed maximum of {self.maximum}"


@dataclass
class MinimumLength(base.Base):
    minimum: int
    length: int

    def __str__(self) -> str:
        return f"length {self.length} is less than the allowed minimum of {self.minimum}"
