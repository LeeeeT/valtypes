from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError
from valtypes.util import resolve_type_args

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["untyped_mapping_to_typed_mapping"]


T_mapping = TypeVar("T_mapping", bound=Mapping[Any, Any])


@convert
def untyped_mapping_to_typed_mapping(
    target_type: type[T_mapping], source: Mapping[object, object], collection: Collection
) -> T_mapping:
    keys_type, values_type = resolve_type_args(target_type, Mapping)
    try:
        return {  # type: ignore
            collection.parse(keys_type, key): collection.parse(values_type, value) for key, value in source.items()
        }
    except ParsingError as e:
        raise ParsingError(target_type, source) from e
