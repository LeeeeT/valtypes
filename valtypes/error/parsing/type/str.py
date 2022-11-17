import re
from dataclasses import dataclass

from . import generic

__all__ = ["Base", "Pattern"]


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class Pattern(Base):
    pattern: re.Pattern[str]
    got: str

    def __str__(self) -> str:
        return f"the value doesn't match the pattern '{self.pattern.pattern}', got: '{self.got}'"
