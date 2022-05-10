import pytest

from valtypes import BaseParsingError, parse


def test_parse_to_choice() -> None:
    """
    It tries to parse a value to each union choice
    """

    assert parse(bool | float | str, "1") is True
    assert parse(bool | float | str, "1.23") == 1.23
    assert parse(bool | float | str, "1.2.3") == "1.2.3"


def test_wrong_value() -> None:
    """
    It throws an error if it can't parse a value to any union choices
    """

    with pytest.raises(BaseParsingError):
        parse(bool | float, "1.2.3")
