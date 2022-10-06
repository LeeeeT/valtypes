from dataclasses import InitVar
from typing import Any

from valtypes import condition
from valtypes.parsing import parser, rule
from valtypes.typing import UnionAlias

from .composite import Composite
from .from_callable import FromCallable
from .object_to_dataclass import ObjectToDataclass
from .object_to_list import ObjectToList
from .to_init_var import ToInitVar
from .to_subclass_of import ToSubclassOf
from .to_union import ToUnion

__all__ = ["default"]


default: Composite[object, Any] = Composite[object, Any].empty()

default.add_to_top(
    rule.Base(ToInitVar(default), condition.InstanceOf(InitVar)),
    rule.Base(ObjectToDataclass(default), condition.dataclass_with_init),
    rule.Base(ToSubclassOf[int, object](int, default), condition.LenientStrictSubclassOf(int)),
    rule.Base(ToSubclassOf[float, object](float, default), condition.LenientStrictSubclassOf(float)),
    rule.Base(ToSubclassOf[str, object](str, default), condition.LenientStrictSubclassOf(str)),
    rule.Base(ToSubclassOf[bytes, object](bytes, default), condition.LenientStrictSubclassOf(bytes)),
    rule.Base(ToSubclassOf[bytearray, object](bytearray, default), condition.LenientStrictSubclassOf(bytearray)),
    rule.Base(ObjectToList(default), condition.LenientStrictAliasOf(list)),
    rule.Base(ToUnion(default), condition.InstanceOf(UnionAlias)),
    rule.Base(FromCallable(parser.ObjectToType), condition.is_class),
)
