from dataclasses import dataclass

from valtypes.error import base

__all__ = ["FractionalNumber"]


@dataclass
class FractionalNumber(base.Base):
    number: float

    def __str__(self) -> str:
        return f"got fractional number: {self.number}"
