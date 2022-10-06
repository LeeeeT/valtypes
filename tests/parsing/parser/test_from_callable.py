from valtypes.parsing.parser import FromCallable


def test_calls_callable() -> None:
    assert FromCallable(int).parse("1") == 1


def test_eq_same_callables() -> None:
    assert FromCallable(int) == FromCallable(int)


def test_eq_different_callables() -> None:
    assert FromCallable(str) != FromCallable(int)


def test_eq_not_implemented() -> None:
    FromCallable(int) != int  # type: ignore
