from typing import SupportsIndex, overload

import valtypes.error.parsing.type.numeric as error
from valtypes.typing import Intable

from . import generic

__all__ = [
    "Maximum",
    "Minimum",
    "Negative",
    "NonNegative",
    "NonPositive",
    "Positive",
]


class InitHook(generic.InitHook, int):
    @overload
    def __init__(self, value: Intable = ..., /):
        ...

    @overload
    def __init__(self, value: bytes | bytearray | str, /, base: SupportsIndex):
        ...

    def __init__(self, value: Intable = 0, /, base: SupportsIndex = 10):
        super().__init__()


class Maximum(InitHook):
    __maximum__: int

    def __init_hook__(self) -> None:
        if self > self.__maximum__:
            raise error.Maximum(self.__maximum__, self)


class Minimum(InitHook):
    __minimum__: int

    def __init_hook__(self) -> None:
        if self < self.__minimum__:
            raise error.Minimum(self.__minimum__, self)


class Positive(Minimum):
    __minimum__ = 1


class NonPositive(Maximum):
    __maximum__ = 0


class Negative(Maximum):
    __maximum__ = -1


class NonNegative(Minimum):
    __minimum__ = 0
