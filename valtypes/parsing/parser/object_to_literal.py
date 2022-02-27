from __future__ import annotations

from typing import TYPE_CHECKING, Any
from typing import _LiteralGenericAlias as LiteralGenericAlias  # type: ignore

from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["object_to_literal"]


@convert
def object_to_literal(target_type: LiteralGenericAlias, source: object, collection: Collection) -> Any:
    for choice in target_type.__args__:
        parsed = collection.parse(type(choice), source)
        if parsed == choice:
            return parsed
    raise ParsingError(target_type, source)
