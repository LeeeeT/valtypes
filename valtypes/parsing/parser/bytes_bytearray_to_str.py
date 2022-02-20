from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["bytes_bytearray_to_str"]


T_str = TypeVar("T_str", bound=str)


@convert
def bytes_bytearray_to_str(target_type: type[T_str], source: bytes | bytearray, collection: Collection) -> T_str:
    return target_type(source.decode())
