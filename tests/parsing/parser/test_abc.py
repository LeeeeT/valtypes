import pytest

from testing.parsing.parser import Const
from valtypes.parsing.parser import Chain


def test_rshift_returns_chain() -> None:
    assert Const(1) >> Const(2) == Chain(Const(1), Const(2))


def test_rshift_returns_not_implemented_if_got_not_parser() -> None:
    with pytest.raises(TypeError):
        Const(2) >> ...  # type: ignore
