from valtypes.parsing import collection
from valtypes.parsing.parser import bytes_bytearray_to_str


def test_bytes() -> None:
    """
    It should decode bytes
    """

    assert bytes_bytearray_to_str.parse(str, b"foo", collection) == "foo"


def test_bytes_to_custom_type() -> None:
    """
    It should decode to subclasses of str
    """

    class MyStr(str):
        pass

    assert isinstance(bytes_bytearray_to_str.parse(MyStr, b"foo", collection), MyStr)


def test_bytearray() -> None:
    """
    It should decode bytearray
    """

    assert bytes_bytearray_to_str.parse(str, bytearray("foo", "utf-8"), collection) == "foo"
