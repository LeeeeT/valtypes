from typing import TypeVar

from valtypes.parsing import parser

from .base import ABC

__all__ = ["Const"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class Const(ABC[object, T_contra, T_co]):
    def __init__(self, parser: parser.ABC[T_contra, T_co]):
        self._parser = parser

    def get_parser_for(self, type: object, /) -> parser.ABC[T_contra, T_co]:
        return self._parser
