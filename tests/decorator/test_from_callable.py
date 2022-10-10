from valtypes.decorator import FromCallable


def test_calls_callable() -> None:
    assert FromCallable(int).decorate("1") == 1


def test_eq_returns_true_if_callables_are_equal() -> None:
    assert FromCallable(int) == FromCallable(int)


def test_eq_returns_false_if_callables_are_different() -> None:
    assert FromCallable(str) != FromCallable(int)


def test_eq_returns_not_implemented_if_got_not_from_callable() -> None:
    FromCallable(int) != ...  # type: ignore
