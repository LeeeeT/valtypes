from typing import ClassVar, SupportsIndex, SupportsInt, overload

import valtypes.error.parsing.int as error
from valtypes.typing import ReadableBuffer, SupportsTrunc

from . import generic

__all__ = [
    "Any",
    "InitHook",
    "Maximum",
    "Minimum",
    "Negative",
    "NonNegative",
    "NonPositive",
    "Positive",
]


Any = int


class InitHook(generic.InitHook, int):
    @overload
    def __init__(self, _: str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc = ..., /):
        ...

    @overload
    def __init__(self, _: str | bytes | bytearray, /, base: SupportsIndex):
        ...

    def __init__(self, _: str | ReadableBuffer | SupportsInt | SupportsIndex | SupportsTrunc = 0, /, base: SupportsIndex = 10):
        super().__init__()


class Maximum(InitHook):
    __maximum__: ClassVar[int]

    def __init_hook__(self) -> None:
        if self > self.__maximum__:
            raise error.Maximum(self.__maximum__, self)


class Minimum(InitHook):
    __minimum__: ClassVar[int]

    def __init_hook__(self) -> None:
        if self < self.__minimum__:
            raise error.Minimum(self.__minimum__, self)


class Positive(Minimum):
    __minimum__: ClassVar[int] = 1


class NonPositive(Maximum):
    __maximum__: ClassVar[int] = 0


class Negative(Maximum):
    __maximum__: ClassVar[int] = -1


class NonNegative(Minimum):
    __minimum__: ClassVar[int] = 0
