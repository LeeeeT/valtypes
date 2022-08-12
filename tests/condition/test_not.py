from valtypes.condition import Is


def test_negates_condition() -> None:
    assert not (~Is(1)).check(1)
    assert (~Is(1)).check(2)


def test_eq_returns_true_if_conditions_are_equal() -> None:
    assert ~Is(1) == ~Is(1)


def test_eq_returns_false_if_conditions_are_not_equal() -> None:
    assert ~Is(1) != ~Is(2)


def test_eq_not_implemented() -> None:
    assert ~Is(1) != 1
