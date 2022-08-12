from valtypes.condition import LenientStrictSubclassOf


def test_returns_true_if_value_is_subclass_of_type() -> None:
    assert LenientStrictSubclassOf(object).check(int)


def test_returns_false_if_value_is_not_subclass_of_type() -> None:
    assert not LenientStrictSubclassOf(int).check(1)
    assert not LenientStrictSubclassOf(float).check(int)


def test_returns_false_if_types_are_the_same() -> None:
    assert not LenientStrictSubclassOf(int).check(int)
