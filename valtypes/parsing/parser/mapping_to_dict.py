from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.parsing.error import ParsingError
from valtypes.typing import GenericAlias
from valtypes.util import resolve_type_args

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["mapping_to_dict"]


T_dict = TypeVar("T_dict", bound=dict[Any, Any])


@convert
def mapping_to_dict(target_type: type[T_dict], source: Mapping[object, object], collection: Collection) -> T_dict:
    keys_type, values_type = (
        resolve_type_args(target_type, dict) if isinstance(target_type, GenericAlias) else (object, object)
    )
    try:
        return target_type(dict(collection.parse(Mapping[keys_type, values_type], source)))  # type: ignore
    except ParsingError as e:
        raise ParsingError(target_type, source) from e
