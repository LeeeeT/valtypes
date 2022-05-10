from __future__ import annotations

from collections.abc import Iterable
from typing import Generic, TypeVar

from valtypes.error import BaseParsingError, CompositeParsingError, NotEnoughItemsError, WrongItemError
from valtypes.parsing.controller import Controller
from valtypes.parsing.util import with_source_type
from valtypes.util import resolve_type_args

__all__ = ["IterableToFixedLengthTuple", "iterable_to_fixed_length_tuple"]


T = TypeVar("T")


class IterableToFixedLengthTuple(Generic[T]):
    def __init__(self, target_type: type[tuple[T, ...]], source: Iterable[object], controller: Controller):
        self._target_type = target_type
        self._source = source
        self._controller = controller
        self._desired_types = resolve_type_args(target_type, tuple)
        self._items: list[T] = []
        self._errors: list[BaseParsingError] = []

    def parse(self) -> tuple[T, ...]:
        self._try_parse()
        self._check_enough_items()
        self._check_for_errors()
        return tuple(self._items)

    def _try_parse(self) -> None:
        for index, (desired_type, item) in enumerate(zip(self._desired_types, self._source)):
            try:
                self._items.append(self._controller.parse(desired_type, item))
            except BaseParsingError as error:
                self._errors.append(WrongItemError(index, error))

    def _check_enough_items(self) -> None:
        if len(self._items) + len(self._errors) != len(self._desired_types):
            self._errors.append(NotEnoughItemsError(len(self._desired_types) - len(self._items) - len(self._errors)))

    def _check_for_errors(self) -> None:
        if self._errors:
            raise CompositeParsingError(self._target_type, tuple(self._errors))


@with_source_type(Iterable)
def iterable_to_fixed_length_tuple(target_type: type[tuple[T, ...]], source: Iterable[object], controller: Controller) -> tuple[T, ...]:
    return IterableToFixedLengthTuple(target_type, source, controller).parse()
