from collections.abc import Mapping
from typing import Generic, TypeVar

from .abc import ABC

__all__ = ["MappingToDict"]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)

F = TypeVar("F")

S = TypeVar("S")


class MappingToDict(ABC[Mapping[S, T_contra], dict[T, F]], Generic[S, T_contra, T, F]):
    def __init__(self, key_parser: ABC[S, T], value_parser: ABC[T_contra, F]):
        self._key_parser = key_parser
        self._value_parser = value_parser

    def parse(self, source: Mapping[S, T_contra], /) -> dict[T, F]:
        return {self._key_parser.parse(key): self._value_parser.parse(value) for key, value in source.items()}

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, MappingToDict):
            return self._key_parser == other._key_parser and self._value_parser == other._value_parser
        return NotImplemented
