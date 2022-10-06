import valtypes.type.generic as type


def test_init() -> None:
    """
    It triggers the hook on instance creation
    """

    class Class(type.InitHook):
        hook_triggered = False

        def __init_hook__(self) -> None:
            self.hook_triggered = True

    assert Class().hook_triggered
