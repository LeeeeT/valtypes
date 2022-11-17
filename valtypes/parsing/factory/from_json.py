from typing import Any

from valtypes import condition
from valtypes.parsing import parser, rule

from .composite import Composite
from .from_callable import FromCallable
from .object_to_dataclass import ObjectToDataclass
from .object_to_list import ObjectToList
from .to_init_var import ToInitVar
from .to_literal import ToLiteral
from .to_subclass_of import ToSubclassOf
from .to_subclass_of_generic import ToSubclassOfGeneric
from .to_union import ToUnion

__all__ = ["from_json"]


from_json: Composite[object, Any] = Composite[object, Any].empty()

object_to_init_var: ToInitVar[object, Any] = ToInitVar(from_json)
object_to_dataclass: ObjectToDataclass = ObjectToDataclass(from_json)
object_to_subclass_of_int: ToSubclassOf[int, object] = ToSubclassOf[int, object](int, from_json)
object_to_subclass_of_float: ToSubclassOf[float, object] = ToSubclassOf[float, object](float, from_json)
object_to_subclass_of_str: ToSubclassOf[str, object] = ToSubclassOf[str, object](str, from_json)
object_to_subclass_of_bytes: ToSubclassOf[bytes, object] = ToSubclassOf[bytes, object](bytes, from_json)
object_to_subclass_of_bytearray: ToSubclassOf[bytearray, object] = ToSubclassOf[bytearray, object](bytearray, from_json)
object_to_list_alias: ObjectToList[Any] = ObjectToList(from_json)
object_to_subclass_of_list_alias: ToSubclassOfGeneric[list[Any], object] = ToSubclassOfGeneric[list[Any], object](list, from_json)
object_to_union_alias: ToUnion[object, Any] = ToUnion(from_json)
object_to_literal: ToLiteral[object, Any] = ToLiteral(from_json)
object_to_type: FromCallable[type, object, Any] = FromCallable(parser.ObjectToType)

from_json.add_to_top(
    rule.Base(object_to_init_var, condition.init_var),
    rule.Base(object_to_dataclass, condition.dataclass_with_init),
    rule.Base(object_to_subclass_of_int, condition.object_is_strict_subclass_of_int),
    rule.Base(object_to_subclass_of_float, condition.object_is_strict_subclass_of_float),
    rule.Base(object_to_subclass_of_str, condition.object_is_strict_subclass_of_str),
    rule.Base(object_to_subclass_of_bytes, condition.object_is_strict_subclass_of_bytes),
    rule.Base(object_to_subclass_of_bytearray, condition.object_is_strict_subclass_of_bytearray),
    rule.Base(object_to_list_alias, condition.object_is_strict_alias_of_list),
    rule.Base(object_to_subclass_of_list_alias, condition.object_is_alias_of_list),
    rule.Base(object_to_union_alias, condition.union_alias),
    rule.Base(object_to_literal, condition.literal_alias),
    rule.Base(object_to_type, condition.builtin_type),
)
