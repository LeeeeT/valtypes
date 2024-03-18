from typing import Any, TypeVar, overload

from . import factory

__all__ = ["parse_json"]


T = TypeVar("T")


@overload
def parse_json(type: type[T], source: object) -> T: ...


@overload
def parse_json(type: object, source: object) -> Any: ...


def parse_json(type: type[T] | object, source: object) -> T | Any:
    return factory.from_json.get_parser_for(type).parse(source)
