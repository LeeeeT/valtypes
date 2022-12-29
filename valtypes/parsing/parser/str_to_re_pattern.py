import re
from re import Pattern

import valtypes.error.parsing.str as error

from .from_callable import FromCallable

__all__ = ["str_to_re_pattern"]


@FromCallable
def str_to_re_pattern(pattern: str) -> Pattern[str]:
    try:
        return re.compile(pattern)
    except re.error:
        raise error.RePatternCompilation(pattern) from None
