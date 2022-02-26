from collections.abc import Iterable, Mapping
from dataclasses import is_dataclass
from typing import Any, TypeVar, overload

from valtypes.condition import FromCallable, Is, IsInstance, IsSubclass
from valtypes.decorator import origin
from valtypes.typing import Floatable, GenericAlias

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
        target_condition=IsInstance(type) & IsSubclass(str),
    ),
    Rule(
        parser.dict_to_dataclass,
        source_type=dict[str, object],
        target_condition=IsInstance(type) & FromCallable(is_dataclass),
    ),
    Rule(parser.float_to_int, source_type=float, target_condition=IsInstance(type) & IsSubclass(int)),
    Rule(
        parser.floatable_to_float,
        source_type=Floatable,
        target_condition=IsInstance(type) & IsSubclass(float),
    ),
    Rule(
        parser.iterable_to_list,
        source_type=Iterable,
        target_condition=IsInstance(type) & IsSubclass(list) | IsInstance(GenericAlias) & origin >> IsSubclass(list),
    ),
    Rule(
        parser.mapping_to_dict,
        source_type=Mapping,
        target_condition=IsInstance(type) & IsSubclass(dict) | IsInstance(GenericAlias) & origin >> IsSubclass(dict),
    ),
    Rule(parser.object_to_str, target_condition=IsInstance(type) & IsSubclass(str)),
    Rule(parser.str_to_bool, source_type=str, target_condition=Is(bool)),
    Rule(
        parser.str_to_bytearray,
        source_type=str,
        target_condition=IsInstance(type) & IsSubclass(bytearray),
    ),
    Rule(parser.str_to_bytes, source_type=str, target_condition=IsInstance(type) & IsSubclass(bytes)),
    Rule(
        parser.untyped_mapping_to_typed_mapping,
        source_type=Mapping,
        target_condition=IsInstance(GenericAlias) & origin >> Is(Mapping),
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
