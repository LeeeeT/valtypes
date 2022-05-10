from ipaddress import IPv6Address

from valtypes import parse


def test() -> None:
    """
    It parses str to ipv6
    """

    assert parse(IPv6Address, "1::2") == IPv6Address("1::2")
