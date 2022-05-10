from __future__ import annotations

from collections.abc import Iterable
from typing import Generic, TypeVar

from valtypes.error import BaseParsingError, CompositeParsingError, WrongItemError
from valtypes.parsing.controller import Controller
from valtypes.parsing.util import with_source_type
from valtypes.util import resolve_type_args

__all__ = ["iterable_to_list"]


T = TypeVar("T")


class IterableToList(Generic[T]):
    def __init__(self, target_type: type[list[T]], source: Iterable[object], controller: Controller):
        self._target_type = target_type
        self._source = source
        self._controller = controller
        self._items: list[T] = []
        self._items_type = resolve_type_args(target_type, list)[0]
        self._errors: list[BaseParsingError] = []

    def parse(self) -> list[T]:
        self._try_parse()
        self._check_for_errors()
        return self._items

    def _try_parse(self) -> None:
        for index, item in enumerate(self._source):
            try:
                self._items.append(self._controller.parse(self._items_type, item))
            except BaseParsingError as error:
                self._errors.append(WrongItemError(index, error))

    def _check_for_errors(self) -> None:
        if self._errors:
            raise CompositeParsingError(self._target_type, tuple(self._errors))


@with_source_type(Iterable)
def iterable_to_list(target_type: type[list[T]], source: Iterable[object], controller: Controller) -> list[T]:
    return IterableToList(target_type, source, controller).parse()
