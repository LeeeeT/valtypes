from collections.abc import Callable
from typing import Generic, TypeVar

from valtypes.parsing import parser

from .abc import ABC

__all__ = ["FromCallable"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

F_contra = TypeVar("F_contra", contravariant=True)


class FromCallable(ABC[T_contra, F_contra, T_co], Generic[T_contra, F_contra, T_co]):
    def __init__(self, callable: Callable[[T_contra], parser.ABC[F_contra, T_co]]):
        self._callable = callable

    def get_parser_for(self, type: T_contra, /) -> parser.ABC[F_contra, T_co]:
        return self._callable(type)
