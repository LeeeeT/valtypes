from regex import Match

from valtypes.type.network import IPv4, Octet

from .from_callable import FromCallable

__all__ = ["match_to_ipv4"]


@FromCallable
def match_to_ipv4(match: Match[str]) -> IPv4:
    raw_octets = match.captures("octet")
    octets = [Octet(octet) for octet in raw_octets]
    return IPv4(*octets)
