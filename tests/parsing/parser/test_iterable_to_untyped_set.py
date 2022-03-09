from valtypes.parsing import collection
from valtypes.parsing.parser import iterable_to_untyped_set


def test() -> None:
    assert iterable_to_untyped_set.parse(set, (1, "2.5", b"3"), collection) == {1, "2.5", b"3"}
