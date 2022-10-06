from typing import cast

import pytest

import valtypes.error.parsing as parsing_error
from valtypes.parsing.parser import ABC, FromCallableReraise, ToUnion

to_int_or_float = ToUnion[float | str, float]([FromCallableReraise(int), FromCallableReraise(float)])


def test_returns_first_successful_parsing_result() -> None:
    assert to_int_or_float.parse(1.6) == 1
    assert to_int_or_float.parse("1.6") == 1.6


def test_raises_if_all_parsers_fail() -> None:
    with pytest.raises(parsing_error.Composite) as info:
        to_int_or_float.parse("a")

    assert info.value == parsing_error.Composite((parsing_error.Parsing("a"), parsing_error.Parsing("a")))


def test_eq_returns_true_if_parsers_are_equal() -> None:
    assert ToUnion(cast(list[ABC[float, float]], [FromCallableReraise(int), FromCallableReraise(float)])) == ToUnion(
        cast(list[ABC[float, float]], [FromCallableReraise(int), FromCallableReraise(float)])
    )


def test_eq_returns_false_if_parsers_are_not_equal() -> None:
    assert ToUnion(cast(list[ABC[float, float]], [FromCallableReraise(int), FromCallableReraise(float)])) != ToUnion(
        cast(list[ABC[float, float]], [FromCallableReraise(float), FromCallableReraise(int)])
    )


def test_eq_returns_not_implemented_if_other_is_not_to_union() -> None:
    assert ToUnion(cast(list[ABC[float, float]], [FromCallableReraise(int), FromCallableReraise(float)])) != 1
