from collections.abc import Callable
from typing import Generic, TypeVar

import valtypes.error.parsing as parsing_error

from .abc import ABC

__all__ = ["FromCallableReraise"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class FromCallableReraise(ABC[T_contra, T_co], Generic[T_contra, T_co]):
    def __init__(self, callable: Callable[[T_contra], T_co]):
        self._callable = callable

    def parse(self, source: T_contra, /) -> T_co:
        try:
            return self._callable(source)
        except Exception as e:
            raise parsing_error.Parsing(source) from e

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, FromCallableReraise):
            return self._callable == other._callable
        return NotImplemented
