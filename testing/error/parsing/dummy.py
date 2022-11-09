from testing.error.dummy import Dummy as BaseDummy
from valtypes.error.parsing import Base as BaseParsing

__all__ = ["Dummy"]


class Dummy(BaseParsing, BaseDummy):
    pass
