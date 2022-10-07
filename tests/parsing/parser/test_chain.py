from testing.parsing.parser import Const, noop


def test_combines_two_parsers() -> None:
    assert (Const(1) >> noop).parse(...) == 1


def test_eq_returns_true_if_parsers_are_equal() -> None:
    assert Const(1) >> Const(2) == Const(1) >> Const(2)


def test_eq_returns_false_if_parsers_are_different() -> None:
    assert Const(1) >> Const(2) != Const(1) >> Const(1)
    assert Const(1) >> Const(2) != Const(2) >> Const(2)


def test_eq_returns_not_implemented_if_got_not_parser() -> None:
    assert Const(1) >> Const(2) != ...
