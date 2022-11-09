from valtypes.decorator import FromCallable


def test_combines_two_parsers() -> None:
    assert (FromCallable(int) >> FromCallable(str)).decorate(1.5) == "1"
