from dataclasses import dataclass

from regex import Match, Pattern

import valtypes.error.parsing.str as error

from .base import ABC

__all__ = ["StrToRegexMatch"]


@dataclass(init=False, repr=False)
class StrToRegexMatch(ABC[str, Match[str]]):
    def __init__(self, pattern: Pattern[str]):
        self._pattern = pattern

    def parse(self, source: str, /) -> Match[str]:
        if match := self._pattern.fullmatch(source):
            return match
        raise error.RegexPatternNoMatch(self._pattern, source)
