from __future__ import annotations

import abc
from collections.abc import Callable
from types import GenericAlias
from typing import Generic, TypeVar

__all__ = ["ABC", "Chain", "FromCallable", "origin"]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ABC(abc.ABC, Generic[T_contra, T_co]):
    @abc.abstractmethod
    def decorate(self, value: T_contra, /) -> T_co:
        pass

    def __rshift__(self, other: ABC[T_co, T], /) -> Chain[T_contra, T]:
        if isinstance(other, ABC):
            return Chain(self, other)
        return NotImplemented


class Chain(ABC[T_contra, T_co], Generic[T_contra, T_co]):
    def __init__(self, first: ABC[T_contra, T], second: ABC[T, T_co]):
        self._first = first
        self._second = second

    def decorate(self, value: T_contra, /) -> T_co:
        return self._second.decorate(self._first.decorate(value))

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, Chain):
            return self._first == other._first and self._second == other._second
        return NotImplemented


class FromCallable(ABC[T_contra, T_co], Generic[T_contra, T_co]):
    def __init__(self, callable: Callable[[T_contra], T_co]):
        self._callable = callable

    def decorate(self, value: T_contra, /) -> T_co:
        return self._callable(value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, FromCallable):
            return self._callable == other._callable
        return NotImplemented


@FromCallable
def origin(alias: GenericAlias, /) -> object:
    return alias.__origin__
