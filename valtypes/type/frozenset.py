from collections.abc import Iterable, Sized
from typing import Generic, TypeVar

from . import generic, sized

__all__ = ["NonEmpty"]


T_co = TypeVar("T_co", covariant=True)


class InitHook(generic.InitHook, frozenset[T_co], Generic[T_co]):
    def __init__(self, iterable: Iterable[T_co] = frozenset(), /):
        super().__init__()


class NonEmpty(sized.NonEmpty, InitHook[T_co], frozenset[T_co], Sized, Generic[T_co]):
    pass
