from valtypes.forward_ref import ForwardRef


def test_evaluate() -> None:
    """
    It evaluates it's argument
    """

    RecursiveRef = ForwardRef["RecursiveRef"]  # type: ignore

    assert RecursiveRef.evaluate() is RecursiveRef
