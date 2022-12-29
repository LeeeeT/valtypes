from dataclasses import dataclass
from typing import TypeVar

import valtypes.error.parsing as error

from .base import ABC

__all__ = ["ObjectToType"]


T_co = TypeVar("T_co", covariant=True)


@dataclass(init=False, repr=False)
class ObjectToType(ABC[object, T_co]):
    _type: type[T_co]

    def __init__(self, type: type[T_co]):
        self._type = type

    def parse(self, source: object, /) -> T_co:
        if isinstance(source, self._type):
            return source
        raise error.WrongType(self._type, source)
