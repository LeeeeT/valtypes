from valtypes.condition import Equals


def test_returns_true_if_values_are_equal() -> None:
    assert Equals(True).check(1)


def test_returns_false_if_values_are_different() -> None:
    assert not Equals(True).check(0)
