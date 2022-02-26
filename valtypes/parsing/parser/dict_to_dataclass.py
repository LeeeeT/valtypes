from __future__ import annotations

from dataclasses import MISSING, fields
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["dict_to_dataclass"]


T = TypeVar("T")


@convert
def dict_to_dataclass(target_type: type[T], source: dict[str, object], collection: Collection) -> T:
    attrs: dict[str, Any] = {}
    for field in fields(target_type):
        try:
            attrs[field.name] = collection.parse(field.type, source[field.name])
        except KeyError:
            if field.default is MISSING and field.default_factory is MISSING:  # type: ignore
                raise ParsingError(target_type, source)
    return target_type(**attrs)