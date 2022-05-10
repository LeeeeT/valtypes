from valtypes.condition import is_variable_length_tuple


def test_not_generic_alias() -> None:
    """
    It returns False if a value is not a generic alias
    """

    assert not is_variable_length_tuple(...)


def test_origin_is_not_tuple() -> None:
    """
    It returns False if an origin is not tuple
    """

    assert not is_variable_length_tuple(list[int])


def test_fixed_length_tuple() -> None:
    """
    It returns False if a value is a generic alias of fixed-length tuple
    """

    assert not is_variable_length_tuple(tuple[int])
    assert not is_variable_length_tuple(tuple[int, int])  # type: ignore


def test_variable_length_tuple() -> None:
    """
    It returns True if a value is a generic alias of variable-length tuple
    """

    assert is_variable_length_tuple(tuple[int, ...])
