from valtypes.parsing.parser import FromCallable


def test_combines_two_parsers() -> None:
    assert (FromCallable(int) >> FromCallable(str)).parse(1.5) == "1"


def test_eq_both_parsers_are_the_same() -> None:
    assert FromCallable(int) >> FromCallable(str) == FromCallable(int) >> FromCallable(str)


def test_eq_first_parser_is_different() -> None:
    assert FromCallable(float) >> FromCallable(str) != FromCallable(int) >> FromCallable(str)


def test_eq_second_parser_is_different() -> None:
    assert FromCallable(int) >> FromCallable(float) != FromCallable(int) >> FromCallable(str)


def test_eq_not_implemented() -> None:
    assert FromCallable(int) >> FromCallable(str) != ...
