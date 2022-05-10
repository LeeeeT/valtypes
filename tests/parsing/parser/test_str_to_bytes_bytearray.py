from valtypes import parse


def test_bytes() -> None:
    """
    It converts str to bytes
    """

    assert parse(bytes, "123") == b"123"


def test_bytearray() -> None:
    """
    It converts str to bytearray
    """

    assert parse(bytearray, "abc") == bytearray("abc", "utf-8")
