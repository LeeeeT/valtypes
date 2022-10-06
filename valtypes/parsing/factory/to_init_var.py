from typing import Any, TypeVar

from valtypes.parsing import parser

from .abc import ABC

__all__ = ["ToInitVar"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ToInitVar(ABC[Any, T_contra, T_co]):
    def __init__(self, factory: ABC[Any, T_contra, T_co]):
        self._factory = factory

    def get_parser_for(self, type: Any, /) -> parser.ABC[T_contra, T_co]:
        return self._factory.get_parser_for(type.type)
