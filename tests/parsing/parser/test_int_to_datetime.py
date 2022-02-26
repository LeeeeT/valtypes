from datetime import datetime

from valtypes.parsing import collection
from valtypes.parsing.parser import int_to_datetime


def test_simple() -> None:
    assert int_to_datetime.parse(datetime, 0, collection) == datetime(1970, 1, 1)