from valtypes.condition import Is


def test_returns_true_if_both_conditions_return_true() -> None:
    assert (Is(1) & Is(1)).check(1)


def test_returns_false_if_one_condition_returns_false() -> None:
    assert not (Is(1) & Is(2)).check(1)


def test_eq_returns_true_if_both_conditions_are_equal() -> None:
    assert (Is(1) & Is(2)) == (Is(1) & Is(2))


def test_eq_returns_false_if_one_condition_is_not_equal() -> None:
    assert (Is(1) & Is(2)) != (Is(1) & Is(3))


def test_eq_not_implemented() -> None:
    assert (Is(1) & Is(2)) != 1
