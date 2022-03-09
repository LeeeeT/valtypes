from valtypes.parsing import collection
from valtypes.parsing.parser import iterable_to_untyped_list


def test() -> None:
    assert iterable_to_untyped_list.parse(list, (1, "2.5", b"3"), collection) == [1, "2.5", b"3"]
