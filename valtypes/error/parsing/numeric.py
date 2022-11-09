from dataclasses import dataclass

from . import generic

__all__ = ["Base", "FractionalNumber"]


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class FractionalNumber(Base):
    number: float

    def __str__(self) -> str:
        return f"got fractional number: {self.number}"
