from collections.abc import Iterable
from typing import Generic, TypeVar

from valtypes.parsing import parser
from valtypes.util import resolve_type_args

from .abc import ABC

__all__ = ["IterableToList"]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)


class IterableToList(ABC[type[list[T]], Iterable[T_contra], list[T]], Generic[T, T_contra]):
    def __init__(self, factory: ABC[object, T_contra, T]):
        self._factory = factory

    def get_parser_for(self, type: type[list[T]], /) -> parser.IterableToList[T_contra, T]:
        (items_type,) = resolve_type_args(type, list)
        return parser.IterableToList(self._factory.get_parser_for(items_type))
