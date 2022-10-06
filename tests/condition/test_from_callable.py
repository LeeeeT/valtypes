from valtypes.condition import FromCallable


def test_calls_callable() -> None:
    assert FromCallable(str.islower).check("a")
    assert not FromCallable(str.islower).check("A")
