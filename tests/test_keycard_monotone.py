"""This module validates the is monotone function"""

from src.keycard_utils import is_monotone
from src.keycard import Keycard


def test_monotonic_keycard():
    """This will check whether the function is monotonic"""
    assert is_monotone(
        Keycard([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])
    ), "Test Failed: Expected is monotone"

    assert is_monotone(Keycard([1])), "Test Failed: Expected is monotone"

    assert is_monotone(
        Keycard([1, 2])
    ), "Test Failed: Expected is monotone"

    assert is_monotone(
        Keycard([2, 1])
    ), "Test Failed: Expected is monotone"

    assert is_monotone(
        Keycard([1, 5, 10, 1100, 1101, 1102, 9001])
    ), "Test Failed: Expected is monotone"

    assert not is_monotone(
        Keycard([-1, -5, -10, -1100, -900, -1101, -1102])
    ), "Test Failed: Expected not monotone"

    assert not is_monotone(
        Keycard([1, 2, 0, 0, 0])
    ), "Test Failed: Expected not monotone"

    assert not is_monotone(
        Keycard([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10])
    ), "Test Failed: Expected not monotone"

    assert is_monotone(
        Keycard([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11])
    ), "Test Failed: Expected is monotone"

    assert not is_monotone(
        Keycard([1, 2, -1, -2, -5])
    ), "Test Failed: Expected not monotone"

    assert not is_monotone(
        Keycard([1, 1, 1, 2, 3, 4, 1])
    ), "Test Failed: Expected not monotone"
