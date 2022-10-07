from abc import ABC
from collections.abc import Sized
from typing import TypeVar

import valtypes.error.parsing.type.sized as error
from valtypes.util import super_endpoint

from . import generic

__all__ = [
    "LengthHook",
    "MaximumLength",
    "MinimumLength",
    "NonEmpty",
]


T = TypeVar("T")


class LengthHook(generic.InitHook, Sized, ABC):
    def __init_hook__(self) -> None:
        self.__length_hook__(len(self))

    @super_endpoint
    def __length_hook__(self, length: int) -> None:
        pass

    def __notify_length_delta__(self, delta: int) -> None:
        self.__length_hook__(len(self) + delta)

    def __notify_length_increments__(self) -> None:
        self.__notify_length_delta__(1)

    def __notify_length_decrements__(self) -> None:
        self.__notify_length_delta__(-1)


class MinimumLength(LengthHook, ABC):
    __minimum_length__: int

    def __length_hook__(self, length: int) -> None:
        if length < self.__minimum_length__:
            raise error.MinimumLength(self.__minimum_length__, length)


class MaximumLength(LengthHook, ABC):
    __maximum_length__: int

    def __length_hook__(self, length: int) -> None:
        if length > self.__maximum_length__:
            raise error.MaximumLength(self.__maximum_length__, length)


class NonEmpty(MinimumLength, ABC):
    __minimum_length__ = 1
