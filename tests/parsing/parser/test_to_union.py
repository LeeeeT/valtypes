import pytest

import testing.error.parsing as testing_error
import valtypes.error.parsing as error
from testing.parsing.parser import AlwaysRaise, Const
from valtypes.parsing.parser import ToUnion


def test_returns_first_successful_parsing_result() -> None:
    assert ToUnion[object, object]([Const(1), AlwaysRaise(error.Base("error"))]).parse(...) == 1
    assert ToUnion[object, object]([AlwaysRaise(error.Base("error")), Const(2)]).parse(...) == 2


def test_raises_error_if_all_parsers_fail() -> None:
    with pytest.raises(error.Composite) as info:
        ToUnion([AlwaysRaise(testing_error.Dummy("error 1")), AlwaysRaise(testing_error.Dummy("error 2"))]).parse(...)

    assert info.value == error.Composite((testing_error.Dummy("error 1"), testing_error.Dummy("error 2")))


def test_eq_returns_true_if_parsers_are_equal() -> None:
    assert ToUnion([Const(1), Const(2)]) == ToUnion([Const(1), Const(2)])


def test_eq_returns_false_if_parsers_are_different() -> None:
    assert ToUnion([Const(1), Const(2)]) != ToUnion([Const(1), Const(1)])
    assert ToUnion([Const(1), Const(2)]) != ToUnion([Const(2), Const(2)])


def test_eq_returns_not_implemented_if_got_not_to_union() -> None:
    assert ToUnion([]) != ...
