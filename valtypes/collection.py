from collections.abc import Iterator
from typing import Any, Generic, TypeVar

__all__ = ["Collection"]


T = TypeVar("T")

T_Collection = TypeVar("T_Collection", bound="Collection[Any]")


class Collection(Generic[T]):
    def __init__(self, items: list[T]):
        self._items = items

    @classmethod
    def empty(cls: type[T_Collection]) -> T_Collection:
        return cls([])

    def add_to_top(self, *items: T) -> None:
        self._items[:0] = items

    def add_to_end(self, *items: T) -> None:
        self._items.extend(items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)
