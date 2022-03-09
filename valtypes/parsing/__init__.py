from collections.abc import Iterable, Mapping
from dataclasses import is_dataclass
from datetime import datetime
from typing import Any, TypeVar
from typing import _LiteralGenericAlias as LiteralGenericAlias  # type: ignore
from typing import overload

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
        target_condition=condition.IsSubclass(str),
    ),
    Rule(
        parser.dict_to_dataclass,
        source_type=dict[str, object],
        target_condition=condition.FromCallable(is_dataclass),
    ),
    Rule(parser.float_to_int, source_type=float, target_condition=condition.IsSubclass(int)),
    Rule(
        parser.floatable_to_float,
        source_type=Floatable,
        target_condition=condition.IsSubclass(float),
    ),
    Rule(parser.int_to_datetime, source_type=int, target_condition=condition.Is(datetime)),
    Rule(
        parser.iterable_to_fixed_length_tuple,
        source_type=Iterable,
        target_condition=condition.is_fixed_length_tuple,
    ),
    Rule(
        parser.iterable_to_typed_frozenset,
        source_type=Iterable,
        target_condition=condition.GenericAliasOf(frozenset),
    ),
    Rule(
        parser.iterable_to_typed_list,
        source_type=Iterable,
        target_condition=condition.GenericAliasOf(list),
    ),
    Rule(
        parser.iterable_to_typed_set,
        source_type=Iterable,
        target_condition=condition.GenericAliasOf(set),
    ),
    Rule(
        parser.iterable_to_untyped_frozenset,
        source_type=Iterable,
        target_condition=condition.IsSubclass(frozenset),
    ),
    Rule(
        parser.iterable_to_untyped_list,
        source_type=Iterable,
        target_condition=condition.IsSubclass(list),
    ),
    Rule(
        parser.iterable_to_untyped_set,
        source_type=Iterable,
        target_condition=condition.IsSubclass(set),
    ),
    Rule(
        parser.iterable_to_variable_length_tuple,
        source_type=Iterable,
        target_condition=condition.is_variable_length_tuple,
    ),
    Rule(
        parser.mapping_to_dict,
        source_type=Mapping,
        target_condition=condition.IsSubclass(dict) | condition.GenericAliasOf(dict),
    ),
    Rule(parser.object_to_literal, target_condition=condition.IsInstance(LiteralGenericAlias)),
    Rule(parser.object_to_str, target_condition=condition.IsSubclass(str)),
    Rule(parser.str_to_bool, source_type=str, target_condition=condition.Is(bool)),
    Rule(
        parser.str_to_bytearray,
        source_type=str,
        target_condition=condition.IsSubclass(bytearray),
    ),
    Rule(parser.str_to_bytes, source_type=str, target_condition=condition.IsSubclass(bytes)),
    Rule(
        parser.untyped_mapping_to_typed_mapping,
        source_type=Mapping,
        target_condition=condition.GenericAliasOf(Mapping),
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
