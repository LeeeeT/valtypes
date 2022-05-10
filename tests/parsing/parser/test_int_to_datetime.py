from datetime import datetime

import pytest

from valtypes import BaseParsingError, parse


def test_timestamp() -> None:
    """
    It converts a timestamp to datetime
    """

    assert parse(datetime, 0) == datetime(1970, 1, 1)


def test_error() -> None:
    """
    It throws an error if it can't convert a timestamp to datetime
    """

    with pytest.raises(BaseParsingError):
        parse(datetime, 99999999999999999999)
