from typing import TypeVar

from valtypes.condition import AliasOf

T = TypeVar("T")


class List(list[T]):
    pass


def test_returns_true_if_value_is_alias_of_type() -> None:
    assert AliasOf(list).check(list[int])
    assert AliasOf(list).check(List[str])


def test_returns_false_if_value_is_not_alias_of_type() -> None:
    assert not AliasOf(list).check(tuple[str, ...])
