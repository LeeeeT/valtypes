from collections.abc import Mapping
from typing import Any, Generic, TypeVar

from valtypes.parsing import parser
from valtypes.util import resolve_type_args

from .abc import ABC

__all__ = ["MappingToDict"]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

F = TypeVar("F")


class MappingToDict(ABC[type[dict[Any, Any]], Mapping[T_contra, T_co], dict[Any, Any]], Generic[T_contra, T_co]):
    def __init__(self, factory: ABC[Any, T_contra | T_co, Any]):
        self._factory = factory

    def get_parser_for(self, type: type[dict[T, F]], /) -> parser.MappingToDict[T_contra, T_co, T, F]:
        keys_type, values_type = resolve_type_args(type, dict)
        return parser.MappingToDict(self._factory.get_parser_for(keys_type), self._factory.get_parser_for(values_type))
