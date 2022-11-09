from valtypes.error import NoParser


def test_no_parser() -> None:
    assert str(NoParser(list[int])) == "there's no parser for list[int]"
