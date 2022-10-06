from valtypes.condition import Is, Shortcut


def test_calls_wrapped_condition() -> None:
    assert Shortcut(Is(42)).check(42)
