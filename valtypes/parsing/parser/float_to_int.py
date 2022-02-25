from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from valtypes.parsing.error import ParsingError

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["float_to_int"]


T_int = TypeVar("T_int", bound=int)


@convert
def float_to_int(target_type: type[T_int], source: float, collection: Collection) -> T_int:
    if source.is_integer():
        try:
            return target_type(int(source))
        except ValueError as e:
            raise ParsingError(target_type, source) from e
    raise ParsingError(target_type, source)
