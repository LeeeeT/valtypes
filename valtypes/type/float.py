from typing import ClassVar, SupportsFloat, SupportsIndex

import valtypes.error.parsing.type.numeric as error
from valtypes.typing import ReadableBuffer

from . import generic

__all__ = [
    "ExclusiveMaximum",
    "ExclusiveMinimum",
    "InitHook",
    "Maximum",
    "Minimum",
    "Negative",
    "NonNegative",
    "NonPositive",
    "Portion",
    "Positive",
]


class InitHook(generic.InitHook, float):
    def __init__(self, x: SupportsFloat | SupportsIndex | str | ReadableBuffer = 0.0, /):
        super().__init__()


class ExclusiveMaximum(InitHook):
    __exclusive_maximum__: ClassVar[float]

    def __init_hook__(self) -> None:
        if self >= self.__exclusive_maximum__:
            raise error.ExclusiveMaximum(self.__exclusive_maximum__, self)


class Maximum(InitHook):
    __maximum__: ClassVar[float]

    def __init_hook__(self) -> None:
        if self > self.__maximum__:
            raise error.Maximum(self.__maximum__, self)


class ExclusiveMinimum(InitHook):
    __exclusive_minimum__: ClassVar[float]

    def __init_hook__(self) -> None:
        if self <= self.__exclusive_minimum__:
            raise error.ExclusiveMinimum(self.__exclusive_minimum__, self)


class Minimum(InitHook):
    __minimum__: ClassVar[float]

    def __init_hook__(self) -> None:
        if self < self.__minimum__:
            raise error.Minimum(self.__minimum__, self)


class Positive(ExclusiveMinimum):
    __exclusive_minimum__: ClassVar[float] = 0.0


class NonPositive(Maximum):
    __maximum__: ClassVar[float] = 0.0


class Negative(ExclusiveMaximum):
    __exclusive_maximum__: ClassVar[float] = 0.0


class NonNegative(Minimum):
    __minimum__: ClassVar[float] = 0.0


class Portion(Minimum, Maximum):
    __minimum__: ClassVar[float] = 0.0
    __maximum__: ClassVar[float] = 1.0
