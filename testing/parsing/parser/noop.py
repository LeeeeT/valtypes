from valtypes.parsing.parser import FromCallable

__all__ = ["noop"]


@FromCallable
def noop(source: object, /) -> object:
    return source
