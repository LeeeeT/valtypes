from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TypeVar

from valtypes.util import get_absolute_name

from .abc import ABC

if TYPE_CHECKING:
    from valtypes.parsing import Collection


__all__ = ["FromCallable", "convert"]


T = TypeVar("T")


class FromCallable(ABC):
    def __init__(self, callable: Callable[[Any, Any, Collection], Any], /):
        self.callable = callable

    def parse(self, target_type: Any, source: Any, collection: Collection) -> Any:
        return self.callable(target_type, source, collection)

    def __repr__(self) -> str:
        return f"{get_absolute_name(self.__class__)}({get_absolute_name(self.callable)})"


def convert(callable: Callable[[Any, Any, Collection], Any], /) -> FromCallable:
    return FromCallable(callable)
