from types import GenericAlias
from typing import cast

from valtypes.condition import fixed_length_tuple_alias


def test_returns_true_if_value_is_fixed_length_tuple_alias() -> None:
    assert fixed_length_tuple_alias.check(cast(GenericAlias, tuple[int, int]))  # type: ignore


def test_returns_false_if_value_is_variable_length_tuple_alias() -> None:
    assert not fixed_length_tuple_alias.check(cast(GenericAlias, tuple[int, ...]))
