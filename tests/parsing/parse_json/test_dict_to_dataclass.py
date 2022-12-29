from dataclasses import KW_ONLY, InitVar, dataclass, field
from typing import ClassVar

import pytest

import valtypes.error.parsing as parsing_error
import valtypes.error.parsing.dataclass as dataclass_parsing_error
from valtypes import error, parse_json


def test_parses_dict_keys_and_values_to_dataclass_fields() -> None:
    @dataclass
    class Foo:
        bar: int
        baz: str

    assert parse_json(Foo, {"bar": 1, "baz": "2"}) == Foo(1, "2")


def test_does_not_require_optional_fields() -> None:
    @dataclass
    class Foo:
        a: int
        _: KW_ONLY
        b: int = field(default=2)
        c: str
        d: str = "d"
        e: int = field(default_factory=lambda: 5)

    assert parse_json(Foo, {"a": 1, "c": "c"}) == Foo(1, c="c")


def test_uses_provided_value_rather_than_default() -> None:
    @dataclass
    class Foo:
        a: int = 1
        b: int = field(default=2)
        c: int = field(default_factory=lambda: 3)

    assert parse_json(Foo, {"a": 4, "b": 5, "c": 6}) == Foo(4, 5, 6)


def test_does_not_require_no_init_fields() -> None:
    @dataclass
    class Foo:
        bar: int = field(init=False)

    parse_json(Foo, {})


def test_does_not_require_class_var_fields() -> None:
    @dataclass
    class Foo:
        bar: ClassVar[int]

    parse_json(Foo, {})


def test_requires_init_var_fields() -> None:
    @dataclass
    class Foo:
        fields: tuple[object, ...] = field(init=False)
        bar: InitVar[str]
        baz: InitVar[int]

        def __post_init__(self, bar: str, baz: int) -> None:
            self.fields = (bar, baz)

    assert parse_json(Foo, {"bar": "bar", "baz": 1}) == Foo("bar", 1)


def test_raises_error_if_dataclass_has_no_init_method() -> None:
    @dataclass(init=False)
    class Foo:
        bar: int

    with pytest.raises(error.NoParser):
        parse_json(Foo, {"bar": 1})


def test_raises_error_if_got_dataclass_instance() -> None:
    @dataclass(unsafe_hash=True)
    class Foo:
        bar: int

    with pytest.raises(error.NoParser) as info:
        parse_json(Foo(1), {"bar": 1})

    assert info.value == error.NoParser(Foo(1))


def test_raises_error_if_required_field_is_missing() -> None:
    @dataclass
    class Foo:
        bar: int
        baz: str

    with pytest.raises(dataclass_parsing_error.Composite) as info:
        parse_json(Foo, {"bar": 1})

    assert info.value == dataclass_parsing_error.Composite([dataclass_parsing_error.MissingField("baz")], {"bar": 1})


def test_raises_error_if_cant_parse_field() -> None:
    @dataclass
    class Foo:
        bar: int
        baz: str

    with pytest.raises(dataclass_parsing_error.Composite) as info:
        parse_json(Foo, {"bar": "1", "baz": 2})

    assert info.value == dataclass_parsing_error.Composite(
        [
            dataclass_parsing_error.WrongFieldValue("bar", parsing_error.WrongType(int, "1"), "1"),
            dataclass_parsing_error.WrongFieldValue("baz", parsing_error.WrongType(str, 2), 2),
        ],
        {"bar": "1", "baz": 2},
    )
