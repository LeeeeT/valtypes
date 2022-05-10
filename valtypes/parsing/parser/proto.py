from __future__ import annotations

from typing import Any, Protocol

from valtypes.parsing.controller import Controller

__all__ = ["Proto"]


class Proto(Protocol):
    def __call__(self, target_type: Any, source: Any, controller: Controller) -> Any:
        ...
