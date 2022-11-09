from valtypes.condition import Is


def test_returns_true_if_both_conditions_return_true() -> None:
    assert (Is(1) & Is(1)).check(1)


def test_returns_false_if_one_condition_returns_false() -> None:
    assert not (Is(1) & Is(2)).check(1)
