from collections.abc import Callable
from typing import Any

from .controller import Controller
from .parser.with_source_type import WithSourceType

__all__ = ["with_source_type"]


def with_source_type(source_type: object) -> Callable[[Callable[[Any, Any, Controller], Any]], Callable[[Any, Any, Controller], Any]]:
    def decorator(parser: Callable[[Any, Any, Controller], Any]) -> Callable[[Any, Any, Controller], Any]:
        return WithSourceType(parser, source_type)

    return decorator
