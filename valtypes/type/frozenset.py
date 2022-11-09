from collections.abc import Iterable
from typing import TypeVar

from . import generic, sized

__all__ = ["InitHook", "MaximumLength", "MinimumLength", "NonEmpty"]


T_co = TypeVar("T_co", covariant=True)


class InitHook(generic.InitHook, frozenset[T_co]):
    def __init__(self, iterable: Iterable[T_co] = frozenset(), /):
        super().__init__()


class MinimumLength(InitHook[T_co], sized.MinimumLength):
    pass


class MaximumLength(InitHook[T_co], sized.MaximumLength):
    pass


class NonEmpty(MinimumLength[T_co], sized.NonEmpty):
    pass
