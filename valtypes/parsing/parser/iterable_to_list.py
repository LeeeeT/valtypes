from collections.abc import Iterable
from typing import Generic, TypeVar

from .abc import ABC

__all__ = ["IterableToList"]


T = TypeVar("T")

F = TypeVar("F")


class IterableToList(ABC[Iterable[F], list[T]], Generic[F, T]):
    def __init__(self, items_parser: ABC[F, T]):
        self._items_parser = items_parser

    def parse(self, source: Iterable[F], /) -> list[T]:
        return [self._items_parser.parse(item) for item in source]
