from valtypes.parsing import collection
from valtypes.parsing.parser import str_to_bytes


def test_simple() -> None:
    assert str_to_bytes.parse(bytes, "string", collection).decode() == "string"


def test_custom_type() -> None:
    class MyBytes(bytes):
        pass

    assert isinstance(str_to_bytes.parse(MyBytes, "string", collection), MyBytes)
