from typing import TypeVar

from valtypes.condition import ObjectIsStrictAliasOf

T = TypeVar("T")


class List(list[T]):
    pass


def test_returns_true_if_alias_origin_is_type() -> None:
    assert ObjectIsStrictAliasOf(list).check(list[int])


def test_returns_false_if_alias_origin_is_not_type() -> None:
    assert not ObjectIsStrictAliasOf(list).check(tuple[str, ...])
    assert not ObjectIsStrictAliasOf(list).check(List[str])
    assert not ObjectIsStrictAliasOf(tuple).check(())
