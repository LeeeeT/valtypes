from typing import Any

from valtypes.parsing.controller import Controller

from .proto import Proto

__all__ = ["WithSourceType"]


class WithSourceType(Proto):
    def __init__(self, parser: Proto, source_type: object):
        self.parser = parser
        self.source_type = source_type

    def __call__(self, target_type: Any, source: object, controller: Controller) -> Any:
        return self.parser(target_type, controller.delegate(self.source_type, source), controller)
