from valtypes.condition import negative, non_negative, non_positive, positive
from valtypes.constrained import ConstrainedFloat, ConstrainedInt

__all__ = [
    "PositiveInt",
    "NonPositiveInt",
    "NegativeInt",
    "NonNegativeInt",
    "PositiveFloat",
    "NonPositiveFloat",
    "NegativeFloat",
    "NonNegativeFloat",
]


class PositiveInt(ConstrainedInt):
    _constraint = positive


class NonPositiveInt(ConstrainedInt):
    _constraint = non_positive


class NegativeInt(ConstrainedInt):
    _constraint = negative


class NonNegativeInt(ConstrainedInt):
    _constraint = non_negative


class PositiveFloat(ConstrainedFloat):
    _constraint = positive


class NonPositiveFloat(ConstrainedFloat):
    _constraint = non_positive


class NegativeFloat(ConstrainedFloat):
    _constraint = negative


class NonNegativeFloat(ConstrainedFloat):
    _constraint = non_negative
