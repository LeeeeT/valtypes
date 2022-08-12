from typing import Generic, TypeVar

from valtypes.parsing import parser

from .abc import ABC
from .iterable_to_list import IterableToList
from .shortcut import Shortcut

__all__ = ["ObjectToList"]


T = TypeVar("T")


class ObjectToList(Shortcut[type[list[T]], object, list[T]], Generic[T]):
    def __init__(self, factory: ABC[object, object, T]):
        super().__init__(parser.ObjectToType(list) >> IterableToList(factory))
