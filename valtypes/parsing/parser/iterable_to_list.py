from collections.abc import Iterable
from typing import Generic, TypeVar

from .abc import ABC

__all__ = ["IterableToList"]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)


class IterableToList(ABC[Iterable[T_contra], list[T]], Generic[T_contra, T]):
    def __init__(self, items_parser: ABC[T_contra, T]):
        self._items_parser = items_parser

    def parse(self, source: Iterable[T_contra], /) -> list[T]:
        return [self._items_parser.parse(item) for item in source]
