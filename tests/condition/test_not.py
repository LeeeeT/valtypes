from valtypes.condition import Is


def test_negates_condition() -> None:
    assert not (~Is(1)).check(1)
    assert (~Is(1)).check(2)
