from dataclasses import dataclass

from valtypes.error.parsing import Base

__all__ = ["Dummy"]


@dataclass
class Dummy(Base):
    message: str
