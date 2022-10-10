import valtypes.type.generic as type


def test_triggers_hook_on_instance_creation() -> None:
    class Class(type.InitHook):
        hook_triggered = False

        def __init_hook__(self) -> None:
            self.hook_triggered = True

    assert Class().hook_triggered
