from valtypes.condition import SubclassOf


def test_returns_true_if_value_is_subclass_of_type() -> None:
    assert SubclassOf(int).check(int)
    assert SubclassOf(object).check(int)


def test_returns_false_if_value_is_not_subclass_of_type() -> None:
    assert not SubclassOf(int).check(object)
    assert not SubclassOf(float).check(int)
