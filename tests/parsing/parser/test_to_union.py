import pytest

import testing.error.parsing as testing_error
import valtypes.error.parsing as error
from testing.parsing.parser import AlwaysRaise, Const
from valtypes.parsing.parser import ToUnion


def test_returns_first_successful_parsing_result() -> None:
    assert ToUnion[object, object]([Const(1), AlwaysRaise(error.Base("error"))]).parse(...) == 1
    assert ToUnion[object, object]([AlwaysRaise(error.Base("error")), Const(2)]).parse(...) == 2


def test_raises_error_if_all_parsers_fail() -> None:
    with pytest.raises(error.Union) as info:
        ToUnion([AlwaysRaise(testing_error.Dummy("error 1")), AlwaysRaise(testing_error.Dummy("error 2"))]).parse(1)

    assert info.value == error.Union([testing_error.Dummy("error 1"), testing_error.Dummy("error 2")], 1)
