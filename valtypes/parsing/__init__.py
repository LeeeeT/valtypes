from dataclasses import is_dataclass
from datetime import datetime
from ipaddress import IPv4Address, IPv6Address
from typing import _LiteralGenericAlias as LiteralGenericAlias  # type: ignore

from valtypes import condition
from valtypes.constrained import Constrained
from valtypes.forward_ref import ForwardRef
from valtypes.typing import Floatable, UnionType

from . import parser
from .collection import Collection
from .controller import Controller
from .rule import Rule
from .util import with_source_type

__all__ = ["Collection", "Controller", "Rule", "collection", "parse", "with_source_type"]


collection = Collection(
    [
        Rule(parser.object_to_type, condition.IsInstance(type)),
        Rule(parser.to_forward_ref, condition.IsInstance(ForwardRef)),
        Rule(parser.to_union, condition.IsInstance(UnionType)),
        Rule(parser.to_literal, condition.IsInstance(LiteralGenericAlias)),
        Rule(parser.bytes_bytearray_to_str, condition.Is(str)),
        Rule(parser.FromCallable(str), condition.Is(str)),
        Rule(parser.str_to_bytes_bytearray, condition.Is(bytes) | condition.Is(bytearray)),
        Rule(parser.WithSourceType(parser.FromCallable(float), Floatable), condition.Is(float)),
        Rule(parser.float_to_int, condition.Is(int)),
        Rule(parser.str_to_bool, condition.Is(bool)),
        Rule(parser.iterable_to_list, condition.StrictGenericAliasOf(list)),
        Rule(parser.list_to_variable_length_tuple, condition.is_variable_length_tuple),
        Rule(parser.iterable_to_fixed_length_tuple, condition.is_fixed_length_tuple),
        Rule(parser.list_to_set, condition.StrictGenericAliasOf(set)),
        Rule(parser.list_to_frozenset, condition.StrictGenericAliasOf(frozenset)),
        Rule(parser.mapping_to_dict, condition.StrictGenericAliasOf(dict)),
        Rule(parser.to_constrained, condition.IsSubclass(Constrained) | condition.GenericAliasOf(Constrained)),
        Rule(parser.WithSourceType(parser.FromCallable(IPv4Address), str), condition.Is(IPv4Address)),
        Rule(parser.WithSourceType(parser.FromCallable(IPv6Address), str), condition.Is(IPv6Address)),
        Rule(parser.WithSourceType(parser.FromCallable(datetime.utcfromtimestamp), int), condition.Is(datetime)),
        Rule(parser.dict_to_dataclass, is_dataclass),
    ],
)

parse = collection.parse
