from dataclasses import dataclass

import pytest

from valtypes import ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import dict_to_dataclass


def test_simple() -> None:
    @dataclass
    class MyDataclass:
        a: bool
        b: str

    assert dict_to_dataclass.parse(MyDataclass, {"a": "true", "b": 0}, collection) == MyDataclass(True, "0")


def test_optional_fields() -> None:
    @dataclass(kw_only=True)
    class MyDataclass:
        a: bool = False
        b: str
        c: int = 0

    assert dict_to_dataclass.parse(MyDataclass, {"b": False, "c": 1.0}, collection) == MyDataclass(b="False", c=1)


def test_error() -> None:
    @dataclass
    class MyDataclass:
        a: bool
        b: str

    with pytest.raises(ParsingError):
        dict_to_dataclass.parse(MyDataclass, {"a": "false"}, collection)
