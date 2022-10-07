import valtypes.error.parsing.type.numeric as error
from valtypes.typing import Floatable

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
    def __init__(self, value: Floatable = 0.0, /):  # type: ignore
        super().__init__()


class ExclusiveMaximum(InitHook):
    __exclusive_maximum__: float

    def __init_hook__(self) -> None:
        if self >= self.__exclusive_maximum__:
            raise error.ExclusiveMaximum(self.__exclusive_maximum__, self)


class Maximum(InitHook):
    __maximum__: float

    def __init_hook__(self) -> None:
        if self > self.__maximum__:
            raise error.Maximum(self.__maximum__, self)


class ExclusiveMinimum(InitHook):
    __exclusive_minimum__: float

    def __init_hook__(self) -> None:
        if self <= self.__exclusive_minimum__:
            raise error.ExclusiveMinimum(self.__exclusive_minimum__, self)


class Minimum(InitHook):
    __minimum__: float

    def __init_hook__(self) -> None:
        if self < self.__minimum__:
            raise error.Minimum(self.__minimum__, self)


class Positive(ExclusiveMinimum):
    __exclusive_minimum__: float = 0.0


class NonPositive(Maximum):
    __maximum__: float = 0.0


class Negative(ExclusiveMaximum):
    __exclusive_maximum__: float = 0.0


class NonNegative(Minimum):
    __minimum__: float = 0.0


class Portion(Minimum, Maximum):
    __minimum__: float = 0.0
    __maximum__: float = 1.0
