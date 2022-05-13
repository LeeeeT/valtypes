from __future__ import annotations

from collections.abc import Callable
from typing import Any

from valtypes.error import ConversionError
from valtypes.parsing.controller import Controller

__all__ = ["FromCallable"]


class FromCallable:
    def __init__(self, callable: Callable[[Any], Any], /):
        self.callable = callable

    def __call__(self, target_type: Any, source: Any, controller: Controller) -> Any:
        try:
            return self.callable(source)
        except Exception:
            raise ConversionError(source, target_type)
