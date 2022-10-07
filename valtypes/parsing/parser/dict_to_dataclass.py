from functools import cached_property
from typing import Any, Generic, TypeVar

import valtypes.error.parsing as error
import valtypes.error.parsing.dataclass as dataclass_error
from valtypes.util import ErrorsCollector

from .abc import ABC

__all__ = ["DictToDataclass", "Parser"]


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)


class DictToDataclass(ABC[dict[str, T], T_co], Generic[T, T_co]):
    def __init__(self, dataclass: type[T_co], required_fields_parsers: dict[str, ABC[T, Any]], optional_fields_parsers: dict[str, ABC[T, Any]]):
        self._dataclass = dataclass
        self._required_fields_parsers = required_fields_parsers
        self._optional_fields_parsers = optional_fields_parsers

    def parse(self, source: dict[str, T], /) -> T_co:
        return Parser(self._dataclass, self._required_fields_parsers, self._optional_fields_parsers, source).parse()


class Parser(Generic[T, T_co]):
    def __init__(
        self,
        dataclass: type[T_co],
        required_fields_parsers: dict[str, ABC[T, Any]],
        optional_fields_parsers: dict[str, ABC[T, Any]],
        source: dict[str, T],
    ):
        self._dataclass = dataclass
        self._required_fields_parsers = required_fields_parsers
        self._optional_fields_parsers = optional_fields_parsers
        self._source = source

    def parse(self) -> T_co:
        self._try_parse()
        self._check_for_errors()
        return self._dataclass(**self._fields)

    def _try_parse(self) -> None:
        for field_name in self._fields_parsers:
            with self._errors_collector:
                self._try_parse_field(field_name)

    def _try_parse_field(self, field_name: str) -> Any:
        if field_name in self._source:
            self._parse_field(field_name)
        elif self._field_required(field_name):
            raise dataclass_error.MissingField(field_name)

    def _field_required(self, field_name: str) -> bool:
        return field_name in self._required_fields_parsers

    def _parse_field(self, field_name: str) -> None:
        try:
            self._fields[field_name] = self._required_fields_parsers[field_name].parse(self._source[field_name])
        except error.Base as e:
            raise dataclass_error.WrongFieldValue(field_name, e)

    def _check_for_errors(self) -> None:
        if self._errors_collector:
            raise error.Composite(tuple(self._errors_collector))

    @cached_property
    def _errors_collector(self) -> ErrorsCollector[error.Base]:
        return ErrorsCollector(error.Base)

    @cached_property
    def _fields_parsers(self) -> dict[str, ABC[T, Any]]:
        return self._required_fields_parsers | self._optional_fields_parsers

    @cached_property
    def _fields(self) -> dict[str, Any]:
        return {}
