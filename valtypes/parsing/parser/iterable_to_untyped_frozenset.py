from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["iterable_to_untyped_frozenset"]


T_frozenset = TypeVar("T_frozenset", bound=frozenset[Any])


@convert
def iterable_to_untyped_frozenset(
    target_type: type[T_frozenset], source: Iterable[object], collection: Collection
) -> T_frozenset:
    try:
        return target_type(collection.parse(frozenset[object], source))
    except ValueError as e:
        raise ParsingError(target_type, source) from e
