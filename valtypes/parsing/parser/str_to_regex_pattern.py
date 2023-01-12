import regex
from regex import Pattern

import valtypes.error.parsing.str as error

from .from_callable import FromCallable

__all__ = ["str_to_regex_pattern"]


@FromCallable
def str_to_regex_pattern(pattern: str) -> Pattern[str]:
    try:
        return regex.compile(pattern)
    except regex.error:
        raise error.RegexPatternCompilation(pattern) from None
