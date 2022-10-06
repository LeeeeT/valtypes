from collections.abc import Callable
from typing import Generic, TypeVar

from .abc import ABC

__all__ = ["FromCallable"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class FromCallable(ABC[T_contra, T_co], Generic[T_contra, T_co]):
    def __init__(self, callable: Callable[[T_contra], T_co]):
        self._callable = callable

    def parse(self, source: T_contra, /) -> T_co:
        return self._callable(source)

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, FromCallable):
            return self._callable == other._callable
        return NotImplemented
