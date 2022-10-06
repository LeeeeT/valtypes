from collections.abc import Mapping
from typing import Any, Generic, TypeVar

from valtypes.parsing import parser
from valtypes.util import resolve_type_args

from .abc import ABC

__all__ = ["MappingToDict"]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)

F = TypeVar("F")

S = TypeVar("S")


class MappingToDict(ABC[type[dict[Any, Any]], Mapping[S, T_co], dict[Any, Any]], Generic[S, T_co]):
    def __init__(self, factory: ABC[Any, S | T_co, Any]):
        self._factory = factory

    def get_parser_for(self, type: type[dict[T, F]], /) -> parser.MappingToDict[S, T_co, T, F]:
        keys_type, values_type = resolve_type_args(type, dict)
        return parser.MappingToDict(self._factory.get_parser_for(keys_type), self._factory.get_parser_for(values_type))
