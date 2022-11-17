from valtypes.condition import ObjectIsSubclassOf


def test_returns_true_if_value_is_subclass_of_type() -> None:
    assert ObjectIsSubclassOf(int).check(int)
    assert ObjectIsSubclassOf(object).check(int)


def test_returns_false_if_value_is_not_subclass_of_type() -> None:
    assert not ObjectIsSubclassOf(int).check(1)
    assert not ObjectIsSubclassOf(float).check(int)
