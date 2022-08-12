from typing import TypeVar

from valtypes.parsing import parser

from .abc import ABC

__all__ = ["Shortcut"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

F_contra = TypeVar("F_contra", contravariant=True)


class Shortcut(ABC[T_contra, F_contra, T_co]):
    def __init__(self, factory: ABC[T_contra, F_contra, T_co]):
        self._factory = factory

    def get_parser_for(self, type: T_contra, /) -> parser.ABC[F_contra, T_co]:
        return self._factory.get_parser_for(type)
