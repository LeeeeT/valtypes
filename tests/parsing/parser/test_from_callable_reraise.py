import pytest

import valtypes.error.parsing as parsing_error
from valtypes.parsing.parser import FromCallableReraise


def test_calls_callable() -> None:
    assert FromCallableReraise(int).parse("1") == 1


def test_reraises_parsing_error() -> None:
    with pytest.raises(parsing_error.Parsing) as info:
        FromCallableReraise(int).parse("a")

    assert info.value == parsing_error.Parsing("a")


def test_eq_same_callables() -> None:
    assert FromCallableReraise(int) == FromCallableReraise(int)


def test_eq_different_callables() -> None:
    assert FromCallableReraise(str) != FromCallableReraise(int)


def test_eq_not_implemented() -> None:
    FromCallableReraise(int) != int  # type: ignore
