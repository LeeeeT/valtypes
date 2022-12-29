from __future__ import annotations

import abc
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

__all__ = ["ABC", "Chain"]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ABC(abc.ABC, Generic[T_contra, T_co]):
    @abc.abstractmethod
    def parse(self, source: T_contra, /) -> T_co:
        pass

    def __rshift__(self, other: ABC[T_co, T]) -> Chain[T_contra, T]:
        if isinstance(other, ABC):
            return Chain(self, other)
        return NotImplemented


@dataclass(init=False, repr=False)
class Chain(ABC[T_contra, T_co]):
    _first: ABC[T_contra, Any]
    _second: ABC[Any, T_co]

    def __init__(self, first: ABC[T_contra, T], second: ABC[T, T_co]):
        self._first = first
        self._second = second

    def parse(self, source: T_contra, /) -> T_co:
        return self._second.parse(self._first.parse(source))
