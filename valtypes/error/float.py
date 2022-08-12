from dataclasses import dataclass

from . import numeric

__all__ = ["ExclusiveMaximum", "ExclusiveMinimum", "Maximum", "Minimum"]


class Maximum(numeric.Maximum[float]):
    pass


class Minimum(numeric.Minimum[float]):
    pass


@dataclass
class ExclusiveMaximum(numeric.Interval):
    exclusive_maximum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be less than {self.exclusive_maximum}, got: {self.got}"


@dataclass
class ExclusiveMinimum(numeric.Interval):
    exclusive_minimum: float
    got: float

    def __str__(self) -> str:
        return f"the value must be greater than {self.exclusive_minimum}, got: {self.got}"
