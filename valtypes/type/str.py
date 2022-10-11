import re

import valtypes.error.parsing.type.str as error

from . import generic, sized

__all__ = ["InitHook", "MaximumLength", "MinimumLength", "NonEmpty", "Pattern"]


class InitHook(generic.InitHook, str):
    def __init__(self, value: object = "", /):
        super().__init__()


class MinimumLength(InitHook, sized.MinimumLength):
    pass


class MaximumLength(InitHook, sized.MaximumLength):
    pass


class NonEmpty(MinimumLength, sized.NonEmpty):
    pass


class Pattern(InitHook):
    __pattern__: re.Pattern[str]

    def __init_hook__(self) -> None:
        if not self.__pattern__.fullmatch(self):
            raise error.Pattern(self.__pattern__, self)
