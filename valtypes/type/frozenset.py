from collections.abc import Iterable
from typing import TypeVar

from . import generic, sized

__all__ = ["Any", "InitHook", "MaximumLength", "MinimumLength", "NonEmpty"]


T_co = TypeVar("T_co", covariant=True)


Any = frozenset[T_co]


class InitHook(generic.InitHook, frozenset[T_co]):
    def __init__(self, _: Iterable[T_co] = frozenset(), /):
        super().__init__()


class MinimumLength(InitHook[T_co], sized.MinimumLength):
    pass


class MaximumLength(InitHook[T_co], sized.MaximumLength):
    pass


class NonEmpty(MinimumLength[T_co], sized.NonEmpty):
    pass
