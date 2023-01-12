from . import comparison

__all__ = ["Base", "ExclusiveMaximum", "ExclusiveMinimum", "Maximum", "Minimum"]


class Base(comparison.Base):
    pass


class Maximum(comparison.Maximum[float], Base):
    pass


class Minimum(comparison.Minimum[float], Base):
    pass


class ExclusiveMaximum(comparison.ExclusiveMaximum[float], Base):
    pass


class ExclusiveMinimum(comparison.ExclusiveMinimum[float], Base):
    pass
