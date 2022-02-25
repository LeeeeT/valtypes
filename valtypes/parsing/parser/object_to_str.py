from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["object_to_str"]


T_str = TypeVar("T_str", bound=str)


@convert
def object_to_str(target_type: type[T_str], source: object, collection: Collection) -> T_str:
    try:
        return target_type(str(source))
    except ValueError as e:
        raise ParsingError(target_type, source) from e
