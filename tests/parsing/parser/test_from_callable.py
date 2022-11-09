from valtypes.parsing.parser import FromCallable


def test_calls_callable() -> None:
    assert FromCallable(int).parse("1") == 1
