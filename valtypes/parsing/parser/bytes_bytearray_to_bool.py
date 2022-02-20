from __future__ import annotations

from typing import TYPE_CHECKING

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["bytes_bytearray_to_bool"]


@convert
def bytes_bytearray_to_bool(target_type: type[bool], source: bytes | bytearray, collection: Collection) -> bool:
    return collection.parse(bool, source.decode())
