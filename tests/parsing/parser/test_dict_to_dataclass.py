from dataclasses import dataclass, field

import pytest

from valtypes import Alias, BaseParsingError, parse


def test_fields_parsing() -> None:
    """
    It parses dict items to the dataclass fields according to their annotations
    """

    @dataclass
    class Dataclass:
        a: bool
        b: str

    assert parse(Dataclass, {"a": "true", "b": 0}) == Dataclass(True, "0")


def test_optional_fields() -> None:
    """
    It supports optional fields
    """

    @dataclass(kw_only=True)
    class Dataclass:
        a: bool = False
        b: str = ""
        c: int = 0

    assert parse(Dataclass, {"b": False, "c": 1.0}) == Dataclass(b="False", c=1)


def test_alias() -> None:
    """
    It supports creating aliases for fields
    """

    @dataclass
    class Dataclass:
        a: bool = field(metadata=Alias("b", "B"))
        b: str = field(metadata=Alias("a", "A"))

    assert parse(Dataclass, {"a": 1, "B": "n"}) == Dataclass(False, "1")


def test_wrong_field() -> None:
    """
    It throws an error if it can't parse some value to the desired field type
    """

    @dataclass
    class Dataclass:
        a: bool

    with pytest.raises(BaseParsingError):
        parse(Dataclass, {"a": "ah yes"})


def test_missing_field() -> None:
    """
    It throws an error if a dict does not have all the required keys
    """

    @dataclass
    class Dataclass:
        a: bool
        b: str

    with pytest.raises(BaseParsingError):
        parse(Dataclass, {"a": "false"})
