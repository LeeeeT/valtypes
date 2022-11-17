from typing import TypeVar

from valtypes.condition import ObjectIsAliasOf

T = TypeVar("T")


class List(list[T]):
    pass


def test_returns_true_if_value_is_alias_of_type() -> None:
    assert ObjectIsAliasOf(list).check(list[int])
    assert ObjectIsAliasOf(list).check(List[str])


def test_returns_false_if_value_is_not_alias_of_type() -> None:
    assert not ObjectIsAliasOf(list).check(tuple[str, ...])
    assert not ObjectIsAliasOf(tuple).check(())
