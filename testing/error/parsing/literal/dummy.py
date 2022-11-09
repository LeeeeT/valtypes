from testing.error.parsing import Dummy as BaseDummy
from valtypes.error.parsing.literal import Base as BaseLiteral

__all__ = ["Dummy"]


class Dummy(BaseLiteral, BaseDummy):
    pass
