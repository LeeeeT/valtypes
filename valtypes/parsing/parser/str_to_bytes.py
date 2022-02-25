from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from .from_callable import convert

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["str_to_bytes"]


T_bytes = TypeVar("T_bytes", bound=bytes)


@convert
def str_to_bytes(target_type: type[T_bytes], source: str, collection: Collection) -> T_bytes:
    return target_type(source.encode())
