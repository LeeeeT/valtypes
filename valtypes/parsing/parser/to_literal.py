from collections.abc import Iterable
from functools import cached_property
from typing import Generic, TypeVar

import valtypes.error.parsing.literal as literal_error

from .abc import ABC
from .to_literal_choice_preparse import ToLiteralChoicePreparse

__all__ = ["ToLiteral"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class ToLiteral(ABC[T_contra, T_co]):
    def __init__(self, choice_parsers: Iterable[ToLiteralChoicePreparse[T_contra, T_co]]):
        self._choice_parsers = choice_parsers

    def parse(self, source: T_contra, /) -> T_co:
        return Parser(self._choice_parsers, source).parse()


class Parser(Generic[T_contra, T_co]):
    def __init__(self, choice_parsers: Iterable[ToLiteralChoicePreparse[T_contra, T_co]], source: T_contra):
        self._choice_parsers = choice_parsers
        self._source = source

    def parse(self) -> T_co:
        for choice_parser in self._choice_parsers:
            try:
                return choice_parser.parse(self._source)
            except literal_error.Base as e:
                self._errors.append(e)
        raise literal_error.Composite(self._errors, self._source)

    @cached_property
    def _errors(self) -> list[literal_error.Base]:
        return []
