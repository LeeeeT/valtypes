import re
from typing import ClassVar

import regex

import valtypes.error.parsing.str as error

from . import generic, sized

__all__ = ["Any", "InitHook", "MaximumLength", "MinimumLength", "NonEmpty", "RePattern", "RegexPattern"]


Any = str


class InitHook(generic.InitHook, str):
    def __init__(self, _: object = "", /):
        super().__init__()


class MinimumLength(InitHook, sized.MinimumLength):
    pass


class MaximumLength(InitHook, sized.MaximumLength):
    pass


class NonEmpty(MinimumLength, sized.NonEmpty):
    pass


class RePattern(InitHook):
    __pattern__: ClassVar[re.Pattern[str]]

    def __init_hook__(self) -> None:
        if not self.__pattern__.fullmatch(self):
            raise error.RePatternNoMatch(self.__pattern__, self)


class RegexPattern(InitHook):
    __pattern__: ClassVar[regex.Pattern[str]]

    def __init_hook__(self) -> None:
        if not self.__pattern__.fullmatch(self):
            raise error.RegexPatternNoMatch(self.__pattern__, self)
