from valtypes import Constrained, condition

__all__ = [
    "NegativeFloat",
    "NegativeInt",
    "NonNegativeFloat",
    "NonNegativeInt",
    "NonPositiveFloat",
    "NonPositiveInt",
    "Portion",
    "PositiveFloat",
    "PositiveInt",
]


class PositiveInt(Constrained[int], int):
    __constraint__ = condition.GreaterThan(0)


class NonPositiveInt(Constrained[int], int):
    __constraint__ = condition.LessEquals(0)


class NegativeInt(Constrained[int], int):
    __constraint__ = condition.LessThan(0)


class NonNegativeInt(Constrained[int], int):
    __constraint__ = condition.GreaterEquals(0)


class PositiveFloat(Constrained[float], float):
    __constraint__ = condition.GreaterThan(0)


class NonPositiveFloat(Constrained[float], float):
    __constraint__ = condition.LessEquals(0)


class NegativeFloat(Constrained[float], float):
    __constraint__ = condition.LessThan(0)


class NonNegativeFloat(Constrained[float], float):
    __constraint__ = condition.GreaterEquals(0)


class Portion(Constrained[float], float):
    __constraint__ = condition.GreaterEquals(0) & condition.LessEquals(1)
