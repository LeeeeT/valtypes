from typing import Generic, Literal, TypeVar

from valtypes.condition import StrictGenericAliasOf

T = TypeVar("T")


def test_not_generic_alias() -> None:
    """
    It returns False if the value isn't a generic alias
    """

    assert not StrictGenericAliasOf(list)([])


def test_origin_is_not_desired_class() -> None:
    """
    It returns False if the origin isn't the desired class
    """

    assert not StrictGenericAliasOf(list)(Literal[1])

    class List(list[T], Generic[T]):
        pass

    assert not StrictGenericAliasOf(list)(List[int])


def test_origin_is_subclass() -> None:
    """
    It returns True if the origin is the desired class
    """

    assert StrictGenericAliasOf(list)(list[int])
