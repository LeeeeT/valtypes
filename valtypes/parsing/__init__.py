from collections.abc import Iterable
from typing import Any, TypeVar, overload

from valtypes import condition
from valtypes.typing import Floatable

from . import parser
from .collection import Collection
from .error import NoParserFoundError, ParsingError
from .rule import Rule

__all__ = ["parse", "collection", "Collection", "NoParserFoundError", "ParsingError", "Rule"]


T = TypeVar("T")


collection = Collection(
    Rule(
        parser.bytes_bytearray_to_str,
        source_type=bytes | bytearray,
        target_condition=condition.IsInstance(type) & condition.IsSubclass(str),
    ),
    Rule(
        parser.float_to_int, source_type=float, target_condition=condition.IsInstance(type) & condition.IsSubclass(int)
    ),
    Rule(
        parser.floatable_to_float,
        source_type=Floatable,
        target_condition=condition.IsInstance(type) & condition.IsSubclass(float),
    ),
    Rule(
        parser.iterable_to_list,
        source_type=Iterable,
        target_condition=condition.IsInstance(type) & condition.IsSubclass(list),
    ),
    Rule(parser.object_to_str, target_condition=condition.IsInstance(type) & condition.IsSubclass(str)),
    Rule(parser.str_to_bool, source_type=str, target_condition=condition.Is(bool)),
    Rule(
        parser.str_to_bytearray,
        source_type=str,
        target_condition=condition.IsInstance(type) & condition.IsSubclass(bytearray),
    ),
    Rule(
        parser.str_to_bytes, source_type=str, target_condition=condition.IsInstance(type) & condition.IsSubclass(bytes)
    ),
)


@overload
def parse(target_type: type[T], source: Any) -> T:
    ...


@overload
def parse(target_type: Any, source: Any) -> Any:
    ...


def parse(target_type: Any, source: Any) -> Any:
    return collection.parse(target_type, source)
