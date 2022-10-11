from collections.abc import Iterable
from typing import Generic, TypeVar

from . import generic, sized

__all__ = ["InitHook", "MaximumLength", "MinimumLength", "NonEmpty"]


T_co = TypeVar("T_co", covariant=True)


class InitHook(generic.InitHook, tuple[T_co, ...], Generic[T_co]):
    def __init__(self, iterable: Iterable[T_co] = (), /):
        super().__init__()


class MinimumLength(InitHook[T_co], sized.MinimumLength, Generic[T_co]):
    pass


class MaximumLength(InitHook[T_co], sized.MaximumLength, Generic[T_co]):
    pass


class NonEmpty(MinimumLength[T_co], sized.NonEmpty, Generic[T_co]):
    pass
