from dataclasses import dataclass, field

import pytest

from valtypes import Alias, ParsingError
from valtypes.parsing import collection
from valtypes.parsing.parser import dict_to_dataclass


def test_fields_parsing() -> None:
    """
    It should parse dict items to dataclass fields according to their annotations
    """

    @dataclass
    class MyDataclass:
        a: bool
        b: str

    assert dict_to_dataclass.parse(MyDataclass, {"a": "true", "b": 0}, collection) == MyDataclass(True, "0")


def test_optional_fields() -> None:
    """
    It should support optional fields
    """

    @dataclass(kw_only=True)
    class MyDataclass:
        a: bool = False
        b: str = ""
        c: int = 0

    assert dict_to_dataclass.parse(MyDataclass, {"b": False, "c": 1.0}, collection) == MyDataclass(b="False", c=1)


def test_alias() -> None:
    """
    It should support creating aliases to fields
    """

    @dataclass
    class MyDataclass:
        a: bool = field(metadata=Alias("b", "B"))
        b: str = field(metadata=Alias("a", "A"))

    assert dict_to_dataclass.parse(MyDataclass, {"a": 1, "B": "n"}, collection) == MyDataclass(False, "1")


def test_error() -> None:
    """
    It should throw an error if the given dict does not have all the required keys
    """

    @dataclass
    class MyDataclass:
        a: bool
        b: str

    with pytest.raises(ParsingError):
        dict_to_dataclass.parse(MyDataclass, {"a": "false"}, collection)
