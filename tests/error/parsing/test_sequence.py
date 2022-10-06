import valtypes.error.parsing.sequence as sequence_parsing_error
from valtypes import error


def test_wrong_item() -> None:
    e = sequence_parsing_error.WrongItem(42, error.Base("cause"))
    assert str(e) == "[42]: cause"


def test_wrong_items_count() -> None:
    e = sequence_parsing_error.WrongItemsCount(1, 2)
    assert str(e) == "1 item(s) expected, but got 2"
