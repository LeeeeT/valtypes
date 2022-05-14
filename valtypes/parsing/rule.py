from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from .controller import Controller

__all__ = ["Rule"]


@dataclass
class Rule:
    parser: Callable[[Any, Any, Controller], Any]
    target_condition: Callable[[object], bool]
