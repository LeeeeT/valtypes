from __future__ import annotations

from types import UnionType
from typing import TYPE_CHECKING, Any

from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["object_to_union"]


@convert
def object_to_union(target_type: UnionType, source: object, collection: Collection) -> Any:
    for choice in target_type.__args__:
        try:
            return collection.parse(choice, source)
        except Exception:
            pass
    raise ParsingError(target_type, source)
