from datetime import datetime

import pytest

from valtypes import BaseParsingError, parse


def test_timestamp() -> None:
    """
    It converts the timestamp to datetime
    """

    assert parse(datetime, 0) == datetime(1970, 1, 1)


def test_error() -> None:
    """
    It raises an error if it can't convert the timestamp to datetime
    """

    with pytest.raises(BaseParsingError):
        parse(datetime, 99999999999999999999)
