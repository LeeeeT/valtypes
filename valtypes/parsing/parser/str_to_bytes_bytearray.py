from __future__ import annotations

from typing import TypeVar

from valtypes.parsing.controller import Controller
from valtypes.parsing.util import with_source_type

__all__ = ["str_to_bytes_bytearray"]


T_bytes_bytearray = TypeVar("T_bytes_bytearray", bytes, bytearray)


@with_source_type(str)
def str_to_bytes_bytearray(target_type: type[T_bytes_bytearray], source: str, controller: Controller) -> T_bytes_bytearray:
    return target_type(source, "utf-8")
