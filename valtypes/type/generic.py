from valtypes.util import AutoCallSuper, super_endpoint

__all__ = ["InitHook"]


class InitHook(AutoCallSuper):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        self.__init_hook__()

    @super_endpoint
    def __init_hook__(self) -> None:
        pass
