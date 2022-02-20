from __future__ import annotations

import abc
from collections.abc import Callable
from typing import Generic, TypeVar, cast

from valtypes.typing import GenericAlias, SupportsGetItem
from valtypes.util import get_absolute_name

__all__ = [
    "ABC",
    "Chain",
    "FromCallable",
    "Item",
    "convert",
    "origin",
]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

F = TypeVar("F")

S = TypeVar("S")


class ABC(abc.ABC, Generic[T_contra, T_co]):
    @abc.abstractmethod
    def decorate(self, value: T_contra, /) -> T_co:
        pass

    def __rshift__(self, other: ABC[T_co, T] | Callable[[T_co], T]) -> ABC[T_contra, T]:
        if not isinstance(other, ABC) and not callable(other):
            return NotImplemented
        if not isinstance(other, ABC):
            other = FromCallable(other)
        return Chain(self, other)

    def __rrshift__(self, other: Callable[[T], T_contra]) -> ABC[T, T_co]:
        if not callable(other):
            return NotImplemented
        return Chain(FromCallable(other), self)


class Chain(ABC[T, F], Generic[T, F]):
    def __init__(self, first: ABC[T, S], second: ABC[S, F]):
        self.first = first
        self.second = second

    def decorate(self, value: T, /) -> F:
        return self.second.decorate(self.first.decorate(value))

    def __repr__(self) -> str:
        return f"{self.first!r} >> {self.second!r}"


class FromCallable(ABC[T, F], Generic[T, F]):
    def __init__(self, callable: Callable[[T], F], /):
        self.callable = callable

    def decorate(self, value: T, /) -> F:
        return self.callable(value)

    def __repr__(self) -> str:
        return get_absolute_name(self.callable)


class Item(ABC[SupportsGetItem[T, F], F], Generic[T, F]):
    def __init__(self, item: T, /):
        self.item = item

    def decorate(self, object: SupportsGetItem[T, F], /) -> F:
        return object[self.item]

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({self.item!r})"


def convert(callable: Callable[[T], F], /) -> FromCallable[T, F]:
    return FromCallable(callable)


@convert
def origin(alias: GenericAlias, /) -> type:
    return cast(type, alias.__origin__)
