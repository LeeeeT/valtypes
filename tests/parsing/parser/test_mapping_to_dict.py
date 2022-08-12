from valtypes.parsing.parser import FromCallableReraise, MappingToDict


def test_eq_returns_true_if_parsers_are_equal() -> None:
    assert MappingToDict(FromCallableReraise(int), FromCallableReraise(str)) == MappingToDict(FromCallableReraise(int), FromCallableReraise(str))


def test_eq_returns_false_if_parsers_are_not_equal() -> None:
    assert MappingToDict(FromCallableReraise(int), FromCallableReraise(str)) != MappingToDict(FromCallableReraise(str), FromCallableReraise(int))


def test_eq_returns_not_implemented_if_other_is_not_mapping_to_union() -> None:
    assert MappingToDict(FromCallableReraise(int), FromCallableReraise(str)) != 1
