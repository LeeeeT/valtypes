from valtypes import parse


def test_bytes() -> None:
    """
    It converts bytes to str
    """

    assert parse(str, b"qwerty") == "qwerty"


def test_bytearray() -> None:
    """
    It converts bytearray to str
    """

    assert parse(str, bytearray("wawawa", "utf-8")) == "wawawa"
