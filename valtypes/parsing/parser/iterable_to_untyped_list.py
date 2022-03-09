from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["iterable_to_untyped_list"]


T_list = TypeVar("T_list", bound=list[Any])


@convert
def iterable_to_untyped_list(target_type: type[T_list], source: Iterable[object], collection: Collection) -> T_list:
    try:
        return target_type(collection.parse(list[object], source))
    except ValueError as e:
        raise ParsingError(target_type, source) from e
