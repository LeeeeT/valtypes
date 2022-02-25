from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from valtypes.parsing.error import ParsingError
from valtypes.typing import Floatable

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["floatable_to_float"]


T_float = TypeVar("T_float", bound=float)


@convert
def floatable_to_float(target_type: type[T_float], source: Floatable, collection: Collection) -> T_float:
    try:
        return target_type(float(source))
    except ValueError as e:
        raise ParsingError(target_type, source) from e
