from valtypes.condition import ObjectIsStrictSubclassOf


def test_returns_true_if_value_is_subclass_of_type() -> None:
    assert ObjectIsStrictSubclassOf(object).check(int)


def test_returns_false_if_value_is_not_subclass_of_type() -> None:
    assert not ObjectIsStrictSubclassOf(int).check(1)
    assert not ObjectIsStrictSubclassOf(float).check(int)


def test_returns_false_if_types_are_the_same() -> None:
    assert not ObjectIsStrictSubclassOf(int).check(int)
