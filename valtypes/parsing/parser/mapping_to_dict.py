from collections.abc import Mapping
from typing import Generic, TypeVar

from .abc import ABC

__all__ = ["MappingToDict"]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

F = TypeVar("F")


class MappingToDict(ABC[Mapping[T_contra, T_co], dict[T, F]], Generic[T_contra, T_co, T, F]):
    def __init__(self, key_parser: ABC[T_contra, T], value_parser: ABC[T_co, F]):
        self._key_parser = key_parser
        self._value_parser = value_parser

    def parse(self, source: Mapping[T_contra, T_co], /) -> dict[T, F]:
        return {self._key_parser.parse(key): self._value_parser.parse(value) for key, value in source.items()}

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, MappingToDict):
            return self._key_parser == other._key_parser and self._value_parser == other._value_parser
        return NotImplemented
