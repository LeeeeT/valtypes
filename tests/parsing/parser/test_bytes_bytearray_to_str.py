from valtypes.parsing import collection
from valtypes.parsing.parser import bytes_bytearray_to_str


def test_simple() -> None:
    assert bytes_bytearray_to_str.parse(str, b"foo", collection) == "foo"


def test_custom_type() -> None:
    class MyStr(str):
        pass

    assert isinstance(bytes_bytearray_to_str.parse(MyStr, b"foo", collection), MyStr)
