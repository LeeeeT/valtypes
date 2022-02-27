from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError
from valtypes.typing import GenericAlias
from valtypes.util import resolve_type_args

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["iterable_to_set"]


T_set = TypeVar("T_set", bound=set[Any])


@convert
def iterable_to_set(target_type: type[T_set], source: Iterable[object], collection: Collection) -> T_set:
    items_type = resolve_type_args(target_type, set)[0] if isinstance(target_type, GenericAlias) else object
    try:
        return target_type({collection.parse(items_type, item) for item in source})
    except ValueError as e:
        raise ParsingError(target_type, source) from e
