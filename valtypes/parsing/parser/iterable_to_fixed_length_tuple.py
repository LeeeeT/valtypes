from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError
from valtypes.typing import GenericAlias
from valtypes.util import resolve_type_args

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["iterable_to_fixed_length_tuple"]


T_tuple = TypeVar("T_tuple", bound=tuple[Any, ...])


@convert
def iterable_to_fixed_length_tuple(
    target_type: type[T_tuple], source: Iterable[object], collection: Collection
) -> T_tuple:
    item_types = resolve_type_args(target_type, tuple)
    try:
        result = tuple(collection.parse(item_type, item) for item_type, item in zip(item_types, source))
        if len(result) != len(item_types):
            raise ParsingError(target_type, source)
        return target_type(result)
    except ValueError as e:
        raise ParsingError(target_type, source) from e
