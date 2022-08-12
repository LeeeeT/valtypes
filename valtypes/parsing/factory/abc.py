from __future__ import annotations

import abc
from typing import Generic, TypeVar

from valtypes.parsing import parser

__all__ = ["ABC", "Preparse"]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

F_co = TypeVar("F_co", covariant=True)
F_contra = TypeVar("F_contra", contravariant=True)


class ABC(abc.ABC, Generic[T_contra, F_contra, T_co]):
    @abc.abstractmethod
    def get_parser_for(self, type: T_contra, /) -> parser.ABC[F_contra, T_co]:
        pass

    def __rrshift__(self, other: parser.ABC[T, F_contra], /) -> Preparse[T_contra, T, T_co]:
        return Preparse(other, self)


class Preparse(ABC[T_contra, F_contra, F_co], Generic[T_contra, F_contra, F_co]):
    def __init__(self, parser: parser.ABC[F_contra, T], factory: ABC[T_contra, T, F_co]):
        self._parser = parser
        self._factory = factory

    def get_parser_for(self, type: T_contra, /) -> parser.ABC[F_contra, F_co]:
        return self._parser >> self._factory.get_parser_for(type)
