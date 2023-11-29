"""This module validates the is monotone function"""

from src.keycard_utils import is_monotone
from src.keycard import Keycard


def test_monotonic_keycard():
    """This will check whether the function is monotonic"""
    assert is_monotone(
        Keycard(
            [-1, -5, -10, -1100, -1100, -1101, -1102, -9001], access_level=any
        )
    ), "Test Failed: Expected is monotone"

    assert is_monotone(
        Keycard([1], access_level=any)
    ), "Test Failed: Expected is monotone"

    assert is_monotone(
        Keycard([1, 2], access_level=any)
    ), "Test Failed: Expected is monotone"

    assert is_monotone(
        Keycard([2, 1], access_level=any)
    ), "Test Failed: Expected is monotone"

    assert is_monotone(
        Keycard([1, 5, 10, 1100, 1101, 1102, 9001], access_level=any)
    ), "Test Failed: Expected is monotone"

    assert not is_monotone(
        Keycard([-1, -5, -10, -1100, -900, -1101, -1102], access_level=any)
    ), "Test Failed: Expected not monotone"

    assert not is_monotone(
        Keycard([1, 2, 0, 0, 0], access_level=any)
    ), "Test Failed: Expected not monotone"

    assert not is_monotone(
        Keycard([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10], access_level=any)
    ), "Test Failed: Expected not monotone"

    assert is_monotone(
        Keycard(
            [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11], access_level=any
        )
    ), "Test Failed: Expected is monotone"

    assert not is_monotone(
        Keycard([1, 2, -1, -2, -5], access_level=any)
    ), "Test Failed: Expected not monotone"

    assert not is_monotone(
        Keycard([1, 1, 1, 2, 3, 4, 1], access_level=any)
    ), "Test Failed: Expected not monotone"
