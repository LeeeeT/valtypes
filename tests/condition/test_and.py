from valtypes.condition import Is


def test_returns_true_if_both_conditions_return_true() -> None:
    assert (Is(1) & Is(1)).check(1)


def test_returns_false_if_one_condition_returns_false() -> None:
    assert not (Is(1) & Is(2)).check(1)


def test_eq_returns_true_if_both_conditions_are_equal() -> None:
    assert (Is(1) & Is(2)) == (Is(1) & Is(2))


def test_eq_returns_false_if_conditions_are_different() -> None:
    assert (Is(1) & Is(2)) != (Is(1) & Is(1))
    assert (Is(1) & Is(2)) != (Is(2) & Is(2))


def test_eq_returns_not_implemented_if_got_not_and() -> None:
    assert (Is(1) & Is(2)) != ...
