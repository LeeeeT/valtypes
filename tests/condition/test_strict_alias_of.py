from typing import TypeVar

from valtypes.condition import StrictAliasOf

T = TypeVar("T")


class List(list[T]):
    pass


def test_returns_true_if_alias_origin_is_type() -> None:
    assert StrictAliasOf(list).check(list[int])


def test_returns_false_if_alias_origin_is_not_type() -> None:
    assert not StrictAliasOf(list).check(tuple[str, ...])
    assert not StrictAliasOf(list).check(List[str])
