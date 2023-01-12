import re

import regex

from valtypes.pattern import network as pattern
from valtypes.type.network import IPv4, IPv6

from .base import Chain
from .mapping_to_dict import MappingToDict
from .match_to_ipv6 import match_to_ipv6
from .object_to_type import ObjectToType
from .str_to_ipv4 import str_to_ipv4
from .str_to_re_pattern import str_to_re_pattern
from .str_to_regex_match import StrToRegexMatch
from .str_to_regex_pattern import str_to_regex_pattern

__all__ = ["object_to_dataclass_fields_dict", "object_to_ipv4", "object_to_ipv6", "object_to_re_pattern", "object_to_regex_pattern"]


object_to_dataclass_fields_dict: Chain[object, dict[str, object]] = ObjectToType(dict) >> MappingToDict(ObjectToType(str), ObjectToType(object))

object_to_re_pattern: Chain[object, re.Pattern[str]] = ObjectToType(str) >> str_to_re_pattern

object_to_regex_pattern: Chain[object, regex.Pattern[str]] = ObjectToType(str) >> str_to_regex_pattern

object_to_ipv4: Chain[object, IPv4] = ObjectToType(str) >> str_to_ipv4

object_to_ipv6: Chain[object, IPv6] = ObjectToType(str) >> StrToRegexMatch(pattern.ipv6) >> match_to_ipv6
