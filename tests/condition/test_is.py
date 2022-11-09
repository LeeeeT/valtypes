from valtypes.condition import Is


def test_returns_true_if_values_are_the_same() -> None:
    assert Is(1).check(1)


def test_returns_false_if_values_are_different() -> None:
    assert not Is(1).check(2)
