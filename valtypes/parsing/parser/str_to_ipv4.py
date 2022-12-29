from valtypes.pattern import network as pattern
from valtypes.type.network import IPv4

from .base import Chain
from .match_to_ipv4 import match_to_ipv4
from .str_to_regex_match import StrToRegexMatch

__all__ = ["str_to_ipv4"]


str_to_ipv4: Chain[str, IPv4] = StrToRegexMatch(pattern.ipv4) >> match_to_ipv4
