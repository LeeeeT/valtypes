import valtypes.error.parsing as error
import valtypes.error.parsing.sequence as sequence_error


def test_wrong_item() -> None:
    e = sequence_error.WrongItem(42, error.Base("cause"))
    assert str(e) == "[42]: cause"


def test_wrong_items_count() -> None:
    e = sequence_error.WrongItemsCount(1, 2)
    assert str(e) == "1 item(s) expected, got 2"
