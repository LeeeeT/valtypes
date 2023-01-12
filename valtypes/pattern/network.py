from regex import Pattern, compile

from valtypes.regex import network as regex

__all__ = [
    "absolute_or_empty_path",
    "absolute_path",
    "fragment",
    "ipv4",
    "ipv6",
    "ipvfuture_content",
    "no_scheme_path",
    "query",
    "reg_name",
    "rootless_path",
    "scheme",
    "user_info",
]


ipv4: Pattern[str] = compile(regex.ipv4)

ipv6: Pattern[str] = compile(regex.ipv6)

ipvfuture_content: Pattern[str] = compile(regex.ipvfuture_content)

scheme: Pattern[str] = compile(regex.scheme)

user_info: Pattern[str] = compile(regex.user_info)

reg_name: Pattern[str] = compile(regex.reg_name)

absolute_or_empty_path: Pattern[str] = compile(regex.absolute_or_empty_path)

absolute_path: Pattern[str] = compile(regex.absolute_path)

no_scheme_path: Pattern[str] = compile(regex.no_scheme_path)

rootless_path: Pattern[str] = compile(regex.rootless_path)

query: Pattern[str] = compile(regex.query)

fragment: Pattern[str] = compile(regex.fragment)
