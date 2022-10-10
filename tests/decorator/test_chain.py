from valtypes.decorator import FromCallable


def test_combines_two_parsers() -> None:
    assert (FromCallable(int) >> FromCallable(str)).decorate(1.5) == "1"


def test_eq_returns_true_if_parsers_are_equal() -> None:
    assert FromCallable(int) >> FromCallable(str) == FromCallable(int) >> FromCallable(str)


def test_eq_returns_false_if_parsers_are_different() -> None:
    assert FromCallable(float) >> FromCallable(str) != FromCallable(int) >> FromCallable(str)
    assert FromCallable(int) >> FromCallable(float) != FromCallable(int) >> FromCallable(str)


def test_eq_returns_not_implemented_if_got_not_chain() -> None:
    assert FromCallable(int) >> FromCallable(str) != ...
