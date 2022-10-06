from collections.abc import Hashable
from typing import Any, TypeVar, cast, overload

from . import factory

__all__ = ["parse"]


T = TypeVar("T")


@overload
def parse(type: type[T], source: object) -> T:
    ...


@overload
def parse(type: object, source: object) -> Any:
    ...


def parse(type: type[T] | object, source: object) -> T | Any:
    return factory.default.get_parser_for(cast(Hashable, type)).parse(source)
