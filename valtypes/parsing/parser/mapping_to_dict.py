from collections.abc import Mapping
from dataclasses import dataclass
from typing import TypeVar

from .abc import ABC

__all__ = ["MappingToDict"]


T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)

F = TypeVar("F")

S = TypeVar("S")


@dataclass(init=False, repr=False)
class MappingToDict(ABC[Mapping[S, T_contra], dict[T, F]]):
    _keys_parser: ABC[S, T]
    _values_parser: ABC[T_contra, F]

    def __init__(self, keys_parser: ABC[S, T], values_parser: ABC[T_contra, F]):
        self._keys_parser = keys_parser
        self._values_parser = values_parser

    def parse(self, source: Mapping[S, T_contra], /) -> dict[T, F]:
        return {self._keys_parser.parse(key): self._values_parser.parse(value) for key, value in source.items()}
