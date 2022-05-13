from collections.abc import Callable
from typing import Any

from .controller import Controller

__all__ = ["Rule"]


class Rule:
    def __init__(self, parser: Callable[[Any, Any, Controller], Any], target_condition: Callable[[object], bool]):
        self.parser = parser
        self.target_condition = target_condition
