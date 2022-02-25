from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["str_to_bytearray"]


T_bytearray = TypeVar("T_bytearray", bound=bytearray)


@convert
def str_to_bytearray(target_type: type[T_bytearray], source: str, collection: Collection) -> T_bytearray:
    return target_type(bytearray(source, "utf-8"))
