from types import GenericAlias
from typing import cast

from valtypes.forward_ref import ForwardRef

List = list


def test_evaluate() -> None:
    """
    It evaluates its argument in the context of the frame where it was created
    """

    Int = int

    RecursiveRef = ForwardRef["List[Int | str]"]  # type: ignore

    assert RecursiveRef.evaluate() == List[Int | str]  # type: ignore


def test_union() -> None:
    """
    It supports union with other types
    """

    assert cast(GenericAlias, ForwardRef["int"] | str).__args__ == (ForwardRef["int"], str)


def test_repr() -> None:
    """
    It returns the code representation
    """

    assert repr(ForwardRef["list[int]"]) == "'list[int]'"
