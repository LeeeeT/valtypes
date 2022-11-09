from typing import Any, cast

from valtypes.forward_ref import ForwardRef

List = list


def test_evaluate_evaluates_refs_argument_in_context_of_frame_where_it_was_created() -> None:
    Int = int

    RecursiveRef = ForwardRef["List[Int | str]"]

    assert RecursiveRef.evaluate() == List[Int | str]


def test_supports_union_with_other_types() -> None:
    assert cast(Any, ForwardRef["int"] | str).__args__ == (ForwardRef["int"], str)


def test_repr_returns_refs_argument_representation() -> None:
    assert repr(ForwardRef["list[int]"]) == "'list[int]'"
