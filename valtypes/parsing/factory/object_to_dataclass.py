from typing import Any

from valtypes.parsing import parser

from .abc import ABC
from .dict_to_dataclass import DictToDataclass
from .shortcut import Shortcut

__all__ = ["ObjectToDataclass"]


class ObjectToDataclass(Shortcut[type, object, Any]):
    def __init__(self, factory: ABC[object, object, Any]):
        super().__init__(parser.object_to_dataclass_fields_dict >> DictToDataclass(factory))
