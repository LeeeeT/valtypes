from collections.abc import Callable
from typing import Any

from valtypes.parsing.controller import Controller

__all__ = ["WithSourceType"]


class WithSourceType:
    def __init__(self, parser: Callable[[Any, Any, Controller], Any], source_type: object):
        self.parser = parser
        self.source_type = source_type

    def __call__(self, target_type: Any, source: object, controller: Controller) -> Any:
        return self.parser(target_type, controller.delegate(self.source_type, source), controller)
