from .abc import ABC, Chain
from .dict_to_dataclass import DictToDataclass
from .from_callable import FromCallable
from .iterable_to_list import IterableToList
from .mapping_to_dict import MappingToDict
from .object_to_type import ObjectToType
from .to_union import ToUnion

__all__ = [
    "ABC",
    "Chain",
    "DictToDataclass",
    "FromCallable",
    "IterableToList",
    "MappingToDict",
    "ObjectToType",
    "ToUnion",
    "object_to_dataclass_fields_dict",
]


object_to_dataclass_fields_dict: Chain[object, dict[str, object]] = ObjectToType(dict) >> MappingToDict(ObjectToType(str), ObjectToType(object))
