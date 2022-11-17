from testing.error.parsing import Dummy as BaseDummy
from valtypes.error.parsing.dataclass import Base as BaseDataclass

__all__ = ["Dummy"]


class Dummy(BaseDataclass, BaseDummy):
    pass
