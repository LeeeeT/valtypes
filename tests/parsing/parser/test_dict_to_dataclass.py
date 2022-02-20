import pytest

from valtypes import Dataclass, ParsingError, static_analysis
from valtypes.parsing import collection
from valtypes.parsing.parser import dict_to_dataclass


def test_simple() -> None:
    @static_analysis
    class MyDataclass(Dataclass):
        a: float
        b: int

    raw = {"a": 3.14, "b": 4}
    parsed = dict_to_dataclass.parse(MyDataclass, raw, collection)

    assert isinstance(parsed, MyDataclass)
    assert parsed.a == 3.14
    assert parsed.b == 4


def test_missing_field() -> None:
    @static_analysis()
    class MyDataclass(Dataclass):
        a: float
        b: int

    with pytest.raises(ParsingError):
        dict_to_dataclass.parse(MyDataclass, {"a": 1}, collection)


def test_fields_parsing() -> None:
    @static_analysis(kw_only=True)
    class MyDataclass(Dataclass):
        a: bool
        b: int

    raw = {"a": "1", "b": "2.0"}
    parsed = dict_to_dataclass.parse(MyDataclass, raw, collection)

    assert parsed.a is True
    assert isinstance(parsed.b, int)
