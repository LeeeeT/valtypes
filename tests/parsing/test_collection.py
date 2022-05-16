from valtypes.condition import Is
from valtypes.parsing import Collection, Rule
from valtypes.parsing.parser import FromCallable


def test_get_parsers_matching_type() -> None:
    """
    It collects all the parsers from the rules where the type matches the rule condition
    """

    collection = Collection([Rule(FromCallable(str), Is(str))])
    assert collection.get_parsers_matching_type(str) == [FromCallable(str)]


def test_clear_cache() -> None:
    """
    It clears the cache when adding a new rule
    """

    collection = Collection([Rule(FromCallable(str), Is(str))])
    collection.get_parsers_matching_type(str)
    collection.add(Rule(FromCallable(str), Is(str)))

    assert collection.get_parsers_matching_type(str) == [FromCallable(str), FromCallable(str)]


def test_register() -> None:
    """
    It adds a rule to the collection
    """

    collection = Collection()
    collection.register(Is(str))(FromCallable(str))

    assert list(collection) == [Rule(FromCallable(str), Is(str))]
