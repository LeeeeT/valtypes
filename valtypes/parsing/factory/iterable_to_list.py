from collections.abc import Iterable
from typing import TypeVar

from valtypes.parsing import parser
from valtypes.util import resolve_type_arguments

from .abc import ABC

__all__ = ["IterableToList"]


T = TypeVar("T")

F = TypeVar("F")


class IterableToList(ABC[type[list[T]], Iterable[F], list[T]]):
    def __init__(self, factory: ABC[object, F, T]):
        self._factory = factory

    def get_parser_for(self, type: type[list[T]], /) -> parser.IterableToList[F, T]:
        items_type = resolve_type_arguments(type, list).__args__[0]
        return parser.IterableToList(self._factory.get_parser_for(items_type))
