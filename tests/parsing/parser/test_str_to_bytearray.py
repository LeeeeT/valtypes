from valtypes.parsing import collection
from valtypes.parsing.parser import str_to_bytearray


def test_simple() -> None:
    assert str_to_bytearray.parse(bytearray, "string", collection).decode() == "string"


def test_custom_type() -> None:
    class MyBytearray(bytearray):
        pass

    assert isinstance(str_to_bytearray.parse(MyBytearray, "string", collection), MyBytearray)
