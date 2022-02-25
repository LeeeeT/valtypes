from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError
from valtypes.typing import GenericAlias
from valtypes.util import resolve_type_args

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["iterable_to_list"]


T_list = TypeVar("T_list", bound=list[Any])


@convert
def iterable_to_list(target_type: type[T_list], source: Iterable[object], collection: Collection) -> T_list:
    items_type = resolve_type_args(target_type, list)[0] if isinstance(target_type, GenericAlias) else object
    try:
        return target_type([collection.parse(items_type, item) for item in source])
    except ValueError as e:
        raise ParsingError(target_type, source) from e
