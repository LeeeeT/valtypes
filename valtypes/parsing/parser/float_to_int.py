from __future__ import annotations

from valtypes.error import FractionalNumberError
from valtypes.parsing.controller import Controller
from valtypes.parsing.util import with_source_type

__all__ = ["float_to_int"]


@with_source_type(float)
def float_to_int(target_type: type[int], source: float, controller: Controller) -> int:
    if source.is_integer():
        return int(source)
    raise FractionalNumberError(source)
