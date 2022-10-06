from types import GenericAlias
from typing import Generic, TypeVar, cast

from valtypes.condition import StrictAliasOf

T = TypeVar("T")


class List(list[T], Generic[T]):
    pass


def test_returns_true_if_alias_origin_is_type() -> None:
    assert StrictAliasOf(list).check(cast(GenericAlias, list[int]))


def test_returns_false_if_alias_origin_is_not_type() -> None:
    assert not StrictAliasOf(list).check(cast(GenericAlias, tuple[str, ...]))
    assert not StrictAliasOf(list).check(cast(GenericAlias, List[str]))
