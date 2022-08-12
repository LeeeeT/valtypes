from typing import Generic, TypeVar

import valtypes.error.parsing as error

from .abc import ABC

__all__ = ["ObjectToType"]


T_co = TypeVar("T_co", covariant=True)


class ObjectToType(ABC[object, T_co], Generic[T_co]):
    def __init__(self, type: type[T_co]):
        self._type = type

    def parse(self, source: object, /) -> T_co:
        if isinstance(source, self._type):
            return source
        raise error.WrongType(source, self._type)

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, ObjectToType):
            return self._type is other._type
        return NotImplemented
