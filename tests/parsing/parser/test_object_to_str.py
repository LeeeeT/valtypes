from valtypes.parsing import collection
from valtypes.parsing.parser import object_to_str


def test_simple() -> None:
    assert object_to_str.parse(str, 42, collection) == "42"

    class MyClass:
        def __str__(self) -> str:
            return "foo"

    assert object_to_str.parse(str, MyClass(), collection) == "foo"


def test_custom_type() -> None:
    class MyStr(str):
        pass

    assert isinstance(object_to_str.parse(MyStr, object(), collection), MyStr)
