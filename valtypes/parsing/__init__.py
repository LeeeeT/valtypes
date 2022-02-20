from collections.abc import Iterable
from types import UnionType
from typing import Any, TypeVar
from typing import _SpecialForm as SpecialForm  # noqa
from typing import overload

from valtypes.dataclass import Dataclass
from valtypes.typing import Floatable

from . import parser
from .collection import Collection
from .error import NoParserFoundError, ParsingError
from .rule import Rule

__all__ = ["parse", "collection", "Collection", "NoParserFoundError", "ParsingError", "Rule"]


T = TypeVar("T")


collection = Collection(
    Rule(parser.bytes_bytearray_to_str, source_type=bytes | bytearray, target_type=str),
    Rule(parser.dict_to_dataclass, source_type=dict, target_type=Dataclass),
    Rule(parser.float_to_int, source_type=float, target_type=int),
    Rule(parser.floatable_to_float, source_type=Floatable, target_type=float),
    Rule(parser.iterable_to_list, source_type=Iterable, target_type=list),
    Rule(parser.str_to_bool, source_type=str, target_type=bool),
    Rule(parser.object_to_special_form, target_type=SpecialForm),
    Rule(parser.object_to_str, target_type=str),
    Rule(parser.object_to_union, target_type=UnionType),
)


@overload
def parse(target_type: type[T], source: Any) -> T:
    ...


@overload
def parse(target_type: Any, source: Any) -> Any:
    ...


def parse(target_type: Any, source: Any) -> Any:
    return collection.parse(target_type, source)
