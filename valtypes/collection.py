from collections.abc import Iterator
from typing import Generic, TypeVar

__all__ = ["Collection"]


T = TypeVar("T")


class Collection(Generic[T]):
    def __init__(self, items: list[T] | None = None):
        self._items: list[T] = [] if items is None else items

    def add(self, *items: T) -> None:
        self._items.extend(items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)
