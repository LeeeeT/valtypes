import re
from typing import Any

import regex

from valtypes import condition
from valtypes.parsing import parser
from valtypes.parsing.rule import Rule
from valtypes.type.network import IPv4, IPv6

from .composite import Composite
from .const import Const
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
object_to_re_pattern: Const[object, re.Pattern[str]] = Const(parser.object_to_re_pattern)
object_to_regex_pattern: Const[object, regex.Pattern[str]] = Const(parser.object_to_regex_pattern)
object_to_ipv4: Const[object, IPv4] = Const(parser.object_to_ipv4)
object_to_ipv6: Const[object, IPv6] = Const(parser.object_to_ipv6)

from_json.add_to_top(
    Rule(object_to_init_var, condition.init_var),
    Rule(object_to_dataclass, condition.dataclass_with_init),
    Rule(object_to_subclass_of_int, condition.object_is_strict_subclass_of_int),
    Rule(object_to_subclass_of_float, condition.object_is_strict_subclass_of_float),
    Rule(object_to_subclass_of_str, condition.object_is_strict_subclass_of_str),
    Rule(object_to_subclass_of_bytes, condition.object_is_strict_subclass_of_bytes),
    Rule(object_to_subclass_of_bytearray, condition.object_is_strict_subclass_of_bytearray),
    Rule(object_to_list_alias, condition.object_is_strict_alias_of_list),
    Rule(object_to_subclass_of_list_alias, condition.object_is_alias_of_list),
    Rule(object_to_union_alias, condition.union_alias),
    Rule(object_to_literal, condition.literal_alias),
    Rule(object_to_type, condition.builtin_type),
    Rule(object_to_re_pattern, condition.re_pattern_alias),
    Rule(object_to_regex_pattern, condition.regex_pattern_alias),
    Rule(object_to_ipv4, condition.ipv4),
    Rule(object_to_ipv6, condition.ipv6),
)
