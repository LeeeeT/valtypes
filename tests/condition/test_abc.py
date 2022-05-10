from valtypes.condition import And, Decorated, Not, Or, false, true


def test_and() -> None:
    """
    It supports __and__
    """

    and_condition = true & str.istitle

    assert isinstance(and_condition, And)
    assert and_condition.conditions == (true, str.istitle)


def test_rand() -> None:
    """
    It supports __rand__
    """

    and_condition = str.istitle & true

    assert isinstance(and_condition, And)
    assert and_condition.conditions == (str.istitle, true)


def test_or() -> None:
    """
    It supports __or__
    """

    or_condition = true | str.istitle  # type: ignore

    assert isinstance(or_condition, Or)
    assert or_condition.conditions == (true, str.istitle)


def test_ror() -> None:
    """
    It supports __ror__
    """

    or_condition = str.istitle | true  # type: ignore

    assert isinstance(or_condition, Or)
    assert or_condition.conditions == (str.istitle, true)


def test_invert() -> None:
    """
    It supports __invert__
    """

    inverted_condition = ~false

    assert isinstance(inverted_condition, Not)
    assert inverted_condition.condition is false


def test_rrshift() -> None:
    """
    It supports __rrshift__
    """

    decorated_condition = len >> false

    assert isinstance(decorated_condition, Decorated)
    assert decorated_condition.decorator == len
    assert decorated_condition.condition is false
