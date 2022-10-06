from typing import Generic, TypeVar

from valtypes.parsing import parser

from .abc import ABC

__all__ = ["ToSubclassOf"]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)


class ToSubclassOf(ABC[type[T], T_contra, T], Generic[T, T_contra]):
    def __init__(self, base: type[T], factory: ABC[type[T], T_contra, T]):
        self._base = base
        self._factory = factory

    def get_parser_for(self, type: type[T], /) -> parser.ABC[T_contra, T]:
        return self._factory.get_parser_for(self._base) >> parser.FromCallable(type)
