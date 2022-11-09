from valtypes.decorator import FromCallable


def test_calls_callable() -> None:
    assert FromCallable(int).decorate("1") == 1
