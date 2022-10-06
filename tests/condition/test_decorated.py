from valtypes import decorator
from valtypes.condition import Is


def test_calls_decorator_before_checking() -> None:
    assert (decorator.FromCallable(int) >> Is(1)).check("1")


def test_eq_returns_true_if_decorators_and_conditions_are_equal() -> None:
    assert (decorator.FromCallable(int) >> Is(1)) == (decorator.FromCallable(int) >> Is(1))


def test_eq_returns_false_if_decorator_is_not_equal() -> None:
    assert not ((decorator.FromCallable(int) >> Is(1)) == (decorator.FromCallable(str) >> Is(1)))


def test_eq_returns_false_if_condition_is_not_equal() -> None:
    assert not ((decorator.FromCallable(int) >> Is(1)) == (decorator.FromCallable(int) >> Is(2)))


def test_eq_not_implemented() -> None:
    assert (decorator.FromCallable(int) >> Is(1)) != 1
