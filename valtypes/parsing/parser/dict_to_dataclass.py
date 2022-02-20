from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar, cast

from valtypes.dataclass import Dataclass
from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["dict_to_dataclass"]


T_Dataclass = TypeVar("T_Dataclass", bound=Dataclass)


@convert
def dict_to_dataclass(target_type: type[T_Dataclass], source: dict[Any, Any], collection: Collection) -> T_Dataclass:
    if source.keys() < cast(dict[str, object], target_type.__all_annotations__).keys():
        raise ParsingError(target_type, source)
    fields = {field: collection.parse(type, source[field]) for field, type in target_type.__all_annotations__.items()}
    return target_type(**fields)
