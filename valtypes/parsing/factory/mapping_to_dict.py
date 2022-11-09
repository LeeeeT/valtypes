from collections.abc import Mapping
from typing import Any, Generic, TypeVar

from valtypes.parsing import parser
from valtypes.util import resolve_type_args

from .abc import ABC

__all__ = ["MappingToDict"]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)

F = TypeVar("F")

S = TypeVar("S")


class MappingToDict(ABC[type[dict[Any, Any]], Mapping[S, T_contra], dict[Any, Any]], Generic[S, T_contra]):
    def __init__(self, factory: ABC[Any, S | T_contra, Any]):
        self._factory = factory

    def get_parser_for(self, type: type[dict[T, F]], /) -> parser.MappingToDict[S, T_contra, T, F]:
        keys_type, values_type = resolve_type_args(type, dict)
        return parser.MappingToDict(self._factory.get_parser_for(keys_type), self._factory.get_parser_for(values_type))
