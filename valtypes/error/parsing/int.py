from . import comparison

__all__ = ["Base", "ExclusiveMaximum", "ExclusiveMinimum", "Maximum", "Minimum"]


class Base(comparison.Base):
    pass


class Maximum(comparison.Maximum[int], Base):
    pass


class Minimum(comparison.Minimum[int], Base):
    pass


class ExclusiveMaximum(comparison.ExclusiveMaximum[int], Base):
    pass


class ExclusiveMinimum(comparison.ExclusiveMinimum[int], Base):
    pass
