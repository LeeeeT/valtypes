from valtypes.condition import InstanceOf


def test_returns_true_if_value_is_instance_of_type() -> None:
    assert InstanceOf(int).check(1)


def test_returns_false_if_value_is_not_instance_of_type() -> None:
    assert not InstanceOf(int).check("1")
