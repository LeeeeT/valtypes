from valtypes import error


def test_no_parser() -> None:
    e = error.NoParser(list)
    assert str(e) == "there's no parser for list"
