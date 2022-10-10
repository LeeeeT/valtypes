from valtypes.condition import LenientSubclassOf


def test_returns_true_if_value_is_subclass_of_type() -> None:
    assert LenientSubclassOf(int).check(int)
    assert LenientSubclassOf(object).check(int)


def test_returns_false_if_value_is_not_subclass_of_type() -> None:
    assert not LenientSubclassOf(int).check(1)
    assert not LenientSubclassOf(float).check(int)
