from dataclasses import dataclass

from .generic import Base

__all__ = ["FractionalNumber"]


@dataclass
class FractionalNumber(Base):
    number: float

    def __str__(self) -> str:
        return f"got fractional number: {self.number}"
