from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError
from valtypes.util import resolve_type_args

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["iterable_to_typed_frozenset"]


T_frozenset = TypeVar("T_frozenset", bound=frozenset[Any])


@convert
def iterable_to_typed_frozenset(
    target_type: type[T_frozenset], source: Iterable[object], collection: Collection
) -> T_frozenset:
    values_type = resolve_type_args(target_type, frozenset)[0]
    try:
        return target_type(frozenset(collection.parse(values_type, item) for item in source))
    except ValueError as e:
        raise ParsingError(target_type, source) from e
