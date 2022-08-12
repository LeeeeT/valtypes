from sys import _getframe as get_frame  # type: ignore

from valtypes.util.frame import get_frame_fallback


def test() -> None:
    """
    It is the same as sys._getframe
    """

    assert get_frame(0) is get_frame_fallback(0)
    assert get_frame(1) is get_frame_fallback(1)
