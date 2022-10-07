from collections.abc import Iterable
from functools import cached_property
from typing import Generic, TypeVar

import valtypes.error.parsing as error
from valtypes.util import ErrorsCollector

from .abc import ABC

__all__ = ["Parser", "ToUnion"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ToUnion(ABC[T_contra, T_co], Generic[T_contra, T_co]):
    def __init__(self, choices: Iterable[ABC[T_contra, T_co]]):
        self._choices = choices

    def parse(self, source: T_contra, /) -> T_co:
        return Parser(self._choices, source).parse()

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, ToUnion):
            return self._choices == other._choices
        return NotImplemented


class Parser(Generic[T_contra, T_co]):
    def __init__(self, choices: Iterable[ABC[T_contra, T_co]], source: T_contra):
        self._choices = choices
        self._source = source

    def parse(self) -> T_co:
        for choice in self._choices:
            with self._errors_collector:
                return choice.parse(self._source)
        raise error.Composite(tuple(self._errors_collector))

    @cached_property
    def _errors_collector(self) -> ErrorsCollector[error.Base]:
        return ErrorsCollector(error.Base)
