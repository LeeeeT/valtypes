import pytest

from valtypes.parsing.parser import Chain, FromCallable


def test_rshift_returns_chain() -> None:
    assert FromCallable(int) >> FromCallable(str) == Chain(FromCallable(int), FromCallable(str))


def test_rshift_not_implemented() -> None:
    with pytest.raises(TypeError):
        FromCallable(int) >> str  # type: ignore
