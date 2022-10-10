from valtypes.condition import Is


def test_returns_true_if_values_are_the_same() -> None:
    assert Is(1).check(1)


def test_returns_false_if_values_are_different() -> None:
    assert not Is(1).check(2)


def test_eq_returns_true_if_objects_are_equal() -> None:
    assert Is(1) == Is(1)


def test_eq_returns_false_if_objects_are_different() -> None:
    assert Is(1) != Is(2)


def test_eq_returns_not_implemented_if_got_not_is() -> None:
    assert Is(1) != ...
