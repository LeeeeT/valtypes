from dataclasses import dataclass
from typing import ClassVar, Final, Literal

from regex import Pattern

from valtypes.pattern import network as pattern

from . import int, str

__all__ = [
    "AbsoluteOrEmptyPath",
    "AbsolutePath",
    "AbsoluteURI",
    "AbsoluteURIWithAuthority",
    "AbsoluteURIWithoutAuthority",
    "Authority",
    "EmptyPath",
    "Fragment",
    "Hexet",
    "Host",
    "IPLiteral",
    "IPv4",
    "IPv6",
    "IPvFuture",
    "IPvFutureContent",
    "IPvFutureVersion",
    "NoSchemePath",
    "Octet",
    "Port",
    "Query",
    "RegName",
    "RelativeReference",
    "RelativeReferenceWithAuthority",
    "RelativeReferenceWithoutAuthority",
    "RootlessPath",
    "Scheme",
    "URI",
    "URIReference",
    "URIWithAuthority",
    "URIWithoutAuthority",
    "UserInfo",
]


class Octet(int.Minimum, int.Maximum):
    __minimum__: ClassVar[int.Any] = 0
    __maximum__: ClassVar[int.Any] = 255


class Hexet(int.Minimum, int.Maximum):
    __minimum__: ClassVar[int.Any] = 0
    __maximum__: ClassVar[int.Any] = 65565

    def __str__(self) -> str.Any:
        return f"{self:x}"


@dataclass(init=False, unsafe_hash=True)
class IPv4:
    octets: tuple[Octet, Octet, Octet, Octet]

    def __init__(self, *octets: * tuple[Octet, Octet, Octet, Octet]):
        self.octets: Final = octets

    @property
    def hexets(self) -> tuple[Hexet, Hexet]:
        return Hexet(self.octets[0] << 0o10 | self.octets[1]), Hexet(self.octets[2] << 0o10 | self.octets[3])

    def __str__(self) -> str.Any:
        return ".".join(map(str.Any, self.octets))


@dataclass(init=False, unsafe_hash=True)
class IPv6:
    hexets: tuple[Hexet, Hexet, Hexet, Hexet, Hexet, Hexet, Hexet, Hexet]

    def __init__(self, *hexets: * tuple[Hexet, Hexet, Hexet, Hexet, Hexet, Hexet, Hexet, Hexet]):
        self.hexets: Final = hexets

    @property
    def ipv4(self) -> IPv4:
        return IPv4(Octet(self.hexets[-2] >> 0o10), Octet(self.hexets[-2] & 0xFF), Octet(self.hexets[-1] >> 0o10), Octet(self.hexets[-1] & 0xFF))

    def __str__(self) -> str.Any:
        return ":".join(map(str.Any, self.hexets))


class IPvFutureVersion(int.NonNegative):
    def __str__(self) -> str.Any:
        return f"v{self:x}"


class IPvFutureContent(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.ipvfuture_content


@dataclass(unsafe_hash=True, frozen=True)
class IPvFuture:
    version: IPvFutureVersion
    content: IPvFutureContent

    def __str__(self) -> str.Any:
        return f"v{self.version}.{self.content}"


class Scheme(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.scheme


class UserInfo(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.user_info


class RegName(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.reg_name


IPLiteral = IPv6 | IPvFuture


Host = IPv4 | IPLiteral | RegName


Port = int.NonNegative


@dataclass(kw_only=True, unsafe_hash=True, frozen=True)
class Authority:
    user_info: UserInfo | None
    host: Host
    port: Port | None

    def __str__(self) -> str.Any:
        user_info_part = "" if self.user_info is None else f"{self.user_info}@"
        host_part = f"[{self.host}]" if isinstance(self.host, IPLiteral) else f"{self.host}"
        port_part = "" if self.port is None else f":{self.port}"
        return f"{user_info_part}{host_part}{port_part}"


class AbsoluteOrEmptyPath(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.absolute_or_empty_path


class AbsolutePath(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.absolute_path


class NoSchemePath(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.no_scheme_path


class RootlessPath(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.rootless_path


EmptyPath = Literal[""]


class Query(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.query


class Fragment(str.RegexPattern):
    __pattern__: ClassVar[Pattern[str.Any]] = pattern.fragment


@dataclass(kw_only=True, unsafe_hash=True, frozen=True)
class AbsoluteURIWithAuthority:
    scheme: Scheme
    authority: Authority
    path: AbsoluteOrEmptyPath
    query: Query | None

    def __str__(self) -> str.Any:
        query_part = "" if self.query is None else f"?{self.query}"
        return f"{self.scheme}://{self.authority}{self.path}{query_part}"


@dataclass(kw_only=True, unsafe_hash=True, frozen=True)
class AbsoluteURIWithoutAuthority:
    scheme: Scheme
    path: AbsolutePath | RootlessPath | EmptyPath
    query: Query | None

    def __str__(self) -> str.Any:
        query_part = "" if self.query is None else f"?{self.query}"
        return f"{self.scheme}:{self.path}{query_part}"


AbsoluteURI = AbsoluteURIWithAuthority | AbsoluteURIWithoutAuthority


@dataclass(kw_only=True, unsafe_hash=True, frozen=True)
class URIWithAuthority:
    scheme: Scheme
    authority: Authority
    path: AbsoluteOrEmptyPath
    query: Query | None
    fragment: Fragment | None

    def __str__(self) -> str.Any:
        query_part = "" if self.query is None else f"?{self.query}"
        fragment_part = "" if self.fragment is None else f"#{self.fragment}"
        return f"{self.scheme}://{self.authority}{self.path}{query_part}{fragment_part}"


@dataclass(kw_only=True, unsafe_hash=True, frozen=True)
class URIWithoutAuthority:
    scheme: Scheme
    path: AbsolutePath | RootlessPath | EmptyPath
    query: Query | None
    fragment: Fragment | None

    def __str__(self) -> str.Any:
        query_part = "" if self.query is None else f"?{self.query}"
        fragment_part = "" if self.fragment is None else f"#{self.fragment}"
        return f"{self.scheme}:{self.path}{query_part}{fragment_part}"


URI = URIWithAuthority | URIWithoutAuthority


@dataclass(kw_only=True, unsafe_hash=True, frozen=True)
class RelativeReferenceWithAuthority:
    authority: Authority
    path: AbsoluteOrEmptyPath
    query: Query | None
    fragment: Fragment | None

    def __str__(self) -> str.Any:
        query_part = "" if self.query is None else f"?{self.query}"
        fragment_part = "" if self.fragment is None else f"#{self.fragment}"
        return f"//{self.authority}{self.path}{query_part}{fragment_part}"


@dataclass(kw_only=True, unsafe_hash=True, frozen=True)
class RelativeReferenceWithoutAuthority:
    path: AbsolutePath | NoSchemePath | EmptyPath
    query: Query | None
    fragment: Fragment | None

    def __str__(self) -> str.Any:
        query_part = "" if self.query is None else f"?{self.query}"
        fragment_part = "" if self.fragment is None else f"#{self.fragment}"
        return f"{self.path}{query_part}{fragment_part}"


RelativeReference = RelativeReferenceWithAuthority | RelativeReferenceWithoutAuthority


URIReference = URI | RelativeReference
