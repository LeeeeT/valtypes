from __future__ import annotations

from types import TracebackType
from typing import TYPE_CHECKING, Any, TypeVar, overload

from valtypes.error import BaseParsingError, CompositeParsingError, NoParserError, ParsingError, RecursiveParsingError

if TYPE_CHECKING:
    from .collection import Collection


__all__ = ["Controller"]


T = TypeVar("T")


class InvolvedTypes:
    _previous_type: object

    def __init__(self) -> None:
        self._involved_types: list[object] = []

    @property
    def previous_type(self) -> object:
        return self._previous_type

    def reset_previous_type(self) -> None:
        self._previous_type = object

    def add(self, type: object) -> None:
        if type in self._involved_types:
            self._previous_type = type
            raise RecursiveParsingError(tuple(self._involved_types))
        self._involved_types.append(type)

    def pop(self) -> None:
        self._previous_type = self._involved_types.pop()

    def additional_type(self, type: object) -> AdditionalType:
        return AdditionalType(self, type)


class AdditionalType:
    def __init__(self, types: InvolvedTypes, additional_type: object):
        self._types = types
        self._additional_type = additional_type

    def __enter__(self) -> None:
        self._types.add(self._additional_type)

    def __exit__(self, exc_type: type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> None:
        self._types.pop()


class Controller:
    def __init__(self, collection: Collection):
        self._collection = collection
        self._involved_types = InvolvedTypes()

    @overload
    def parse(self, target_type: type[T], source: object) -> T:
        ...

    @overload
    def parse(self, target_type: object, source: object) -> Any:
        ...

    def parse(self, target_type: object, source: object) -> Any:
        return self._collection.parse(target_type, source)

    @overload
    def delegate(self, target_type: type[T], source: object) -> T:
        ...

    @overload
    def delegate(self, target_type: object, source: object) -> Any:
        ...

    def delegate(self, target_type: object, source: object) -> Any:
        with self._involved_types.additional_type(target_type):
            errors: list[BaseParsingError] = []
            for parser in self._collection.get_parsers_matching_type(target_type):
                self._involved_types.reset_previous_type()
                try:
                    return parser(target_type, source, self)
                except BaseParsingError as e:
                    errors.append(ParsingError(self._involved_types.previous_type, target_type, e))
            if errors:
                raise CompositeParsingError(target_type, tuple(errors))
            raise NoParserError(source, target_type)
