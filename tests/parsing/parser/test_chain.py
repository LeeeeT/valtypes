from testing.parsing.parser import Const, noop


def test_combines_two_parsers() -> None:
    assert (Const(1) >> noop).parse(...) == 1
