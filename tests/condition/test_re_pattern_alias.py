import re

import regex

from valtypes.condition import re_pattern_alias


def test_returns_true_if_value_is_re_pattern_alias() -> None:
    assert re_pattern_alias.check(re.Pattern[str])


def test_returns_false_if_value_is_not_re_pattern_alias() -> None:
    assert not re_pattern_alias.check(regex.Pattern[str])
    assert not re_pattern_alias.check(re.Pattern[bytes])
