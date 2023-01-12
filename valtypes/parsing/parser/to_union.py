from collections.abc import Iterable
from dataclasses import dataclass
from functools import cached_property
from typing import Generic, TypeVar

import valtypes.error.parsing as error

from .base import ABC

__all__ = ["Parser", "ToUnion"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


@dataclass(init=False, repr=False)
class ToUnion(ABC[T_contra, T_co]):
    _choice_parsers: Iterable[ABC[T_contra, T_co]]

    def __init__(self, choice_parsers: Iterable[ABC[T_contra, T_co]]):
        self._choice_parsers = choice_parsers

    def parse(self, source: T_contra, /) -> T_co:
        return Parser(self._choice_parsers, source).parse()


class Parser(Generic[T_contra, T_co]):
    def __init__(self, choice_parsers: Iterable[ABC[T_contra, T_co]], source: T_contra):
        self._choice_parsers = choice_parsers
        self._source = source

    def parse(self) -> T_co:
        for choice_parser in self._choice_parsers:
            try:
                return choice_parser.parse(self._source)
            except error.Base as e:
                self._errors.append(e)
        raise error.Union(self._errors, self._source)

    @cached_property
    def _errors(self) -> list[error.Base]:
        return []
