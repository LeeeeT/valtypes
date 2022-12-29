import re

import regex

from valtypes.error.parsing.str import RegexPatternCompilation, RegexPatternNoMatch, RePatternCompilation, RePatternNoMatch


def test_re_pattern_no_match() -> None:
    assert str(RePatternNoMatch(re.compile(r"^[a-z]+$"), "123")) == "the value doesn't match the pattern '^[a-z]+$', got: '123'"


def test_regex_pattern_no_match() -> None:
    assert str(RegexPatternNoMatch(regex.compile(r"^[a-z]+$"), "123")) == "the value doesn't match the pattern '^[a-z]+$', got: '123'"


def test_re_pattern_compilation() -> None:
    assert str(RePatternCompilation("pattern")) == "can't compile pattern 'pattern'"


def test_regex_pattern_compilation() -> None:
    assert str(RegexPatternCompilation("pattern")) == "can't compile pattern 'pattern'"
