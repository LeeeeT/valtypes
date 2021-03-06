from typing import Generic, Literal, TypeVar

from valtypes.condition import GenericAliasOf

T = TypeVar("T")


def test_not_generic_alias() -> None:
    """
    It returns False if the value isn't a generic alias
    """

    assert not GenericAliasOf(list)([])


def test_origin_is_not_subclass() -> None:
    """
    It returns False if the origin isn't a subclass of the desired class
    """

    assert not GenericAliasOf(list)(tuple[int])
    assert not GenericAliasOf(list)(Literal[1, 2, 3])


def test_origin_is_subclass() -> None:
    """
    It returns True if the origin is a subclass of the desired class
    """

    assert GenericAliasOf(list)(list[int])

    class List(list[T], Generic[T]):
        pass

    assert GenericAliasOf(list)(List[int])
