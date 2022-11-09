from dataclasses import dataclass

from valtypes.error import Base

__all__ = ["Dummy"]


@dataclass(repr=False, frozen=True)
class Dummy(Base):
    message: str
