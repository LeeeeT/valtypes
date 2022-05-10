from __future__ import annotations

from dataclasses import MISSING, Field, fields
from typing import Any, Generic, TypeVar

from valtypes.alias import ALIASES_KEY
from valtypes.error import BaseParsingError, CompositeParsingError, MissingFieldError, WrongFieldError
from valtypes.parsing.controller import Controller
from valtypes.parsing.util import with_source_type

__all__ = ["DictToDataclass", "dict_to_dataclass"]


T = TypeVar("T")


class DictToDataclass(Generic[T]):
    def __init__(self, target_type: type[T], source: dict[str, object], controller: Controller) -> None:
        self._target_type = target_type
        self._source = source
        self._controller = controller
        self._fields: dict[str, object] = {}
        self._errors: list[BaseParsingError] = []

    def parse(self) -> T:
        self._collect_fields()
        if self._errors:
            raise CompositeParsingError(self._target_type, tuple(self._errors))
        return self._target_type(**self._fields)

    def _collect_fields(self) -> None:
        for field in fields(self._target_type):
            value = self._try_find_value_for_field(field)
            if value is not MISSING:
                self._try_add_field_value(field, value)

    def _try_add_field_value(self, field: Field[Any], value: object) -> None:
        try:
            self._fields[field.name] = self._controller.parse(field.type, value)
        except BaseParsingError as e:
            self._errors.append(WrongFieldError(field.name, e))

    def _try_find_value_for_field(self, field: Field[Any]) -> object:
        value = self._find_value_for_field(field)
        if value is MISSING and self._is_field_required(field):
            self._errors.append(MissingFieldError(field.name))
        return value

    def _find_value_for_field(self, field: Field[Any]) -> object:
        for alias in self._get_aliases(field):
            if alias in self._source:
                return self._source[alias]
        return MISSING

    @staticmethod
    def _get_aliases(field: Field[Any]) -> tuple[str, ...]:
        return field.metadata.get(ALIASES_KEY, (field.name,))

    @staticmethod
    def _is_field_required(field: Field[Any]) -> bool:
        return field.default is MISSING and field.default_factory is MISSING


@with_source_type(dict[str, object])
def dict_to_dataclass(target_type: type[T], source: dict[str, object], controller: Controller) -> T:
    return DictToDataclass(target_type, source, controller).parse()
