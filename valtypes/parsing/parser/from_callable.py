from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TypeVar

from .abc import ABC

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["FromCallable", "convert"]


T = TypeVar("T")


class FromCallable(ABC):
    def __init__(self, callable: Callable[[Any, Any, Collection], Any], /):
        self.callable = callable

    def parse(self, target_type: Any, value: Any, collection: Collection) -> Any:
        return self.callable(target_type, value, collection)


def convert(callable: Callable[[Any, Any, Collection], Any], /) -> FromCallable:
    return FromCallable(callable)
