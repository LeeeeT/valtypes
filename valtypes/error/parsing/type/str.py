import re
from dataclasses import dataclass

from valtypes.error.generic import Base

__all__ = ["Pattern"]


@dataclass
class Pattern(Base):
    pattern: re.Pattern[str]
    got: str

    def __str__(self) -> str:
        return f"the value doesn't match the pattern {self.pattern.pattern!r}, got: {self.got!r}"
