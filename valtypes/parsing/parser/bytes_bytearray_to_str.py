from __future__ import annotations

from valtypes.parsing.controller import Controller
from valtypes.parsing.util import with_source_type

__all__ = ["bytes_bytearray_to_str"]


@with_source_type(bytes | bytearray)
def bytes_bytearray_to_str(target_type: type[str], source: bytes | bytearray, controller: Controller) -> str:
    return source.decode()
