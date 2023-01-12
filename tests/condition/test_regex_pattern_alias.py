import re

import regex

from valtypes.condition import regex_pattern_alias


def test_returns_true_if_value_is_regex_pattern_alias() -> None:
    assert regex_pattern_alias.check(regex.Pattern[str])


def test_returns_false_if_value_is_not_regex_pattern_alias() -> None:
    assert not regex_pattern_alias.check(re.Pattern[str])
    assert not regex_pattern_alias.check(regex.Pattern[bytes])
