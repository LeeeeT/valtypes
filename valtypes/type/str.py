import re

import valtypes.error.str as error

from . import generic, sized

__all__ = ["InitHook", "LengthHook", "MaximumLength", "MinimumLength", "NonEmpty", "Pattern"]


class InitHook(generic.InitHook, str):
    def __init__(self, value: object = "", /):
        super().__init__()


class LengthHook(InitHook, sized.LengthHook):
    pass


class MinimumLength(LengthHook, sized.MinimumLength):
    pass


class MaximumLength(LengthHook, sized.MaximumLength):
    pass


class NonEmpty(MinimumLength, sized.NonEmpty):
    pass


class Pattern(InitHook):
    __pattern__: re.Pattern[str]

    def __init_hook__(self) -> None:
        if not self.__pattern__.fullmatch(self):
            raise error.Pattern(self.__pattern__, self)
