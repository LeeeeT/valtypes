from __future__ import annotations

from types import TracebackType
from typing import TYPE_CHECKING, Any, TypeVar, overload

from valtypes.error import BaseParsingError, CompositeParsingError, NoParserError, ParsingError

if TYPE_CHECKING:
    from .collection import Collection


__all__ = ["Controller"]


T = TypeVar("T")


class InvolvedTypes:
    def __init__(self) -> None:
        self._involved_types: list[object] = []
        self._last_type: object = object

    @property
    def last(self) -> object:
        return self._last_type

    def add(self, type: object, /) -> None:
        self._involved_types.append(type)

    def pop(self) -> None:
        self._last_type = self._involved_types.pop()

    def additional_type(self, type: object, /) -> AdditionalType:
        return AdditionalType(self, type)

    def __contains__(self, item: object) -> bool:
        return item in self._involved_types


class AdditionalType:
    def __init__(self, types: InvolvedTypes, additional_type: object):
        self._types = types
        self._additional_type = additional_type

    def __enter__(self) -> InvolvedTypes:
        self._types.add(self._additional_type)
        return self._types

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType) -> None:
        self._types.pop()


class Controller:
    def __init__(self, collection: Collection):
        self._collection = collection
        self._involved_types = InvolvedTypes()
        self._last_type: object = object

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
        if target_type not in self._involved_types:
            with self._involved_types.additional_type(target_type):
                errors: list[BaseParsingError] = []
                for parser in self._collection.get_parsers_matching_type(target_type):
                    try:
                        return parser(target_type, source, self)
                    except BaseParsingError as e:
                        errors.append(ParsingError(self._involved_types.last, target_type, e))
                if errors:
                    raise CompositeParsingError(target_type, tuple(errors))
        raise NoParserError(source, target_type)
