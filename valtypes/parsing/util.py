from collections.abc import Callable

from .parser.proto import Proto
from .parser.with_source_type import WithSourceType

__all__ = ["with_source_type"]


def with_source_type(source_type: object) -> Callable[[Proto], Proto]:
    def decorator(parser: Proto) -> Proto:
        return WithSourceType(parser, source_type)

    return decorator
