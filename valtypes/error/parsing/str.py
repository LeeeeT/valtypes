import re
from dataclasses import dataclass

import regex

from . import generic

__all__ = ["Base", "RePatternNoMatch", "RegexPatternNoMatch"]


class Base(generic.Base):
    pass


@dataclass(repr=False, frozen=True)
class RePatternNoMatch(Base):
    pattern: re.Pattern[str]
    got: str

    def __str__(self) -> str:
        return f"the value doesn't match the pattern '{self.pattern.pattern}', got: '{self.got}'"


@dataclass(repr=False, frozen=True)
class RegexPatternNoMatch(Base):
    pattern: regex.Pattern[str]
    got: str

    def __str__(self) -> str:
        return f"the value doesn't match the pattern '{self.pattern.pattern}', got: '{self.got}'"


@dataclass(repr=False, frozen=True)
class RePatternCompilation(Base):
    got: str

    def __str__(self) -> str:
        return f"can't compile pattern '{self.got}'"


@dataclass(repr=False, frozen=True)
class RegexPatternCompilation(Base):
    got: str

    def __str__(self) -> str:
        return f"can't compile pattern '{self.got}'"
