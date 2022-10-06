from types import GenericAlias
from typing import cast

from valtypes.decorator import origin


def test_returns_generic_alias_origin() -> None:
    assert origin.decorate(cast(GenericAlias, list[int])) is list
    assert origin.decorate(cast(GenericAlias, tuple[str, ...])) is tuple
