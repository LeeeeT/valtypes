import re

from valtypes.condition import Pattern


def test_not_matches() -> None:
    """
    It returns False if a values does not match the pattern
    """

    assert not Pattern(re.compile(r"^a$"))("abc")


def test_matches() -> None:
    """
    It returns True if a value matches the pattern
    """

    assert Pattern(re.compile(r"a"))("abc")
