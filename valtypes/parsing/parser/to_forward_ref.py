from __future__ import annotations

from typing import Any

from valtypes.forward_ref import ForwardRef
from valtypes.parsing.controller import Controller

__all__ = ["to_forward_ref"]


def to_forward_ref(target_type: ForwardRef, source: object, controller: Controller) -> Any:
    return controller.delegate(target_type.evaluate(), source)
