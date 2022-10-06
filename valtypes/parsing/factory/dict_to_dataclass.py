from collections.abc import Iterator
from dataclasses import _FIELD_CLASSVAR as FIELD_CLASSVAR_MARKER  # type: ignore
from dataclasses import MISSING, Field
from functools import cached_property
from typing import Any, Generic, TypeVar, cast

from valtypes.parsing import parser

from .abc import ABC

__all__ = ["DictToDataclass", "Factory"]


T = TypeVar("T")

F = TypeVar("F")


class DictToDataclass(ABC[type, dict[str, F], Any], Generic[F]):
    def __init__(self, factory: ABC[object, F, Any]):
        self._factory = factory

    def get_parser_for(self, type: type[T], /) -> parser.DictToDataclass[F, T]:
        return Factory(self._factory, type).get_parser()


class Factory(Generic[F, T]):
    def __init__(self, factory: ABC[object, F, Any], type: type[T]):
        self._factory = factory
        self._type = type

    def get_parser(self) -> parser.DictToDataclass[F, T]:
        self._collect_parsers()
        return parser.DictToDataclass(self._type, self._required_fields_parsers, self._optional_fields_parsers)

    def _collect_parsers(self) -> None:
        for field in self._fields:
            if field.default is field.default_factory is MISSING:
                self._required_fields_parsers[field.name] = self._factory.get_parser_for(field.type)
            else:
                self._optional_fields_parsers[field.name] = self._factory.get_parser_for(field.type)

    @property
    def _fields(self) -> Iterator[Field[object]]:
        for field in cast(Any, self._type).__dataclass_fields__.values():
            if field.init and field._field_type is not FIELD_CLASSVAR_MARKER:
                yield field

    @cached_property
    def _required_fields_parsers(self) -> dict[str, parser.ABC[F, Any]]:
        return {}

    @cached_property
    def _optional_fields_parsers(self) -> dict[str, parser.ABC[F, Any]]:
        return {}
