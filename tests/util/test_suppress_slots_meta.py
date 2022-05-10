from valtypes.util import SuppressSlotsMeta


def test_multiple_inheritance() -> None:
    """
    It allows multiple inheritance from classes with __slots__ defined
    """

    class A(int, metaclass=SuppressSlotsMeta):
        pass

    class B(int, metaclass=SuppressSlotsMeta):
        pass

    class AB(A, B):
        pass
