from collections.abc import Callable
from dataclasses import dataclass
from typing import TypeVar

from .abc import ABC

__all__ = ["FromCallable"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


@dataclass(init=False, repr=False)
class FromCallable(ABC[T_contra, T_co]):
    _callable: Callable[[T_contra], T_co]

    def __init__(self, callable: Callable[[T_contra], T_co]):
        self._callable = callable

    def parse(self, source: T_contra, /) -> T_co:
        return self._callable(source)
