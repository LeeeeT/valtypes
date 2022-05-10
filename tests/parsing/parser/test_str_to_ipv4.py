from ipaddress import IPv4Address

from valtypes import parse


def test() -> None:
    """
    It parses str to ipv4
    """

    assert parse(IPv4Address, "127.0.0.1") == IPv4Address("127.0.0.1")
