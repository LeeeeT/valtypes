from types import UnionType
from typing import Any, TypeVar

from valtypes.parsing import parser

from .abc import ABC

__all__ = ["ToUnion"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ToUnion(ABC[UnionType, T_contra, T_co]):
    def __init__(self, factory: ABC[Any, T_contra, T_co]):
        self._factory = factory

    def get_parser_for(self, type: UnionType, /) -> parser.ToUnion[T_contra, T_co]:
        return parser.ToUnion([self._factory.get_parser_for(choice) for choice in type.__args__])
