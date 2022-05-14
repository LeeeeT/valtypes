from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from valtypes.error import ConversionError
from valtypes.parsing.controller import Controller

__all__ = ["FromCallable"]


@dataclass
class FromCallable:
    callable: Callable[[Any], Any]

    def __call__(self, target_type: Any, source: Any, controller: Controller) -> Any:
        try:
            return self.callable(source)
        except Exception:
            raise ConversionError(source, target_type)
