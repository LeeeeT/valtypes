from collections.abc import Iterable
from functools import cached_property
from typing import Generic, TypeVar

import valtypes.error.parsing as error
import valtypes.error.parsing.sequence as sequence_error

from .abc import ABC

__all__ = ["IterableToList", "Parser"]


T = TypeVar("T")

F = TypeVar("F")


class IterableToList(ABC[Iterable[F], list[T]]):
    def __init__(self, items_parser: ABC[F, T]):
        self._items_parser = items_parser

    def parse(self, source: Iterable[F], /) -> list[T]:
        return Parser(self._items_parser, source).parse()


class Parser(Generic[F, T]):
    def __init__(self, items_parser: ABC[F, T], source: Iterable[F]):
        self._items_parser = items_parser
        self._source = source

    def parse(self) -> list[T]:
        self._try_parse()
        self._check_for_errors()
        return self._items

    def _try_parse(self) -> None:
        for index, item in enumerate(self._source):
            try:
                self._items.append(self._items_parser.parse(item))
            except error.Base as e:
                self._errors.append(sequence_error.WrongItem(index, e, item))

    def _check_for_errors(self) -> None:
        if self._errors:
            raise sequence_error.Composite(self._errors, self._source)

    @cached_property
    def _items(self) -> list[T]:
        return []

    @cached_property
    def _errors(self) -> list[sequence_error.Base]:
        return []
