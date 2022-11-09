from valtypes import decorator
from valtypes.condition import Is


def test_calls_decorator_before_checking() -> None:
    assert (decorator.FromCallable(int) >> Is(1)).check("1")
