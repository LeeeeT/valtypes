from types import GenericAlias
from typing import Generic, TypeVar, cast

from valtypes.condition import AliasOf

T = TypeVar("T")


class List(list[T], Generic[T]):
    pass


def test_returns_true_if_value_is_alias_of_type() -> None:
    assert AliasOf(list).check(cast(GenericAlias, list[int]))
    assert AliasOf(list).check(cast(GenericAlias, List[str]))


def test_returns_false_if_value_is_not_alias_of_type() -> None:
    assert not AliasOf(list).check(cast(GenericAlias, tuple[str, ...]))
