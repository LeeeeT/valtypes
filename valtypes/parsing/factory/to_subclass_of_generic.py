from typing import Any, TypeVar

from valtypes.parsing import parser
from valtypes.util import resolve_type_arguments

from .abc import ABC

__all__ = ["ToSubclassOfGeneric"]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)


class ToSubclassOfGeneric(ABC[type[T], T_contra, T]):
    def __init__(self, base: type[T], factory: ABC[type[T], T_contra, T]):
        self._base: Any = base
        self._factory = factory

    def get_parser_for(self, alias: type[T], /) -> parser.ABC[T_contra, T]:
        return self._factory.get_parser_for(resolve_type_arguments(alias, self._base)) >> parser.FromCallable(alias)
