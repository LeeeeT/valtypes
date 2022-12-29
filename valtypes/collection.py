from collections.abc import Iterator
from typing import Generic, Self, TypeVar

__all__ = ["Collection"]


T = TypeVar("T")


class Collection(Generic[T]):
    def __init__(self, items: list[T]):
        self._items = items

    @classmethod
    def empty(cls) -> Self:
        return cls([])

    def add_to_top(self, *items: T) -> None:
        self._items[:0] = items

    def add_to_end(self, *items: T) -> None:
        self._items.extend(items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)
