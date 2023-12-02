"""This module checks whether the input contains secret number or not"""

from src.keycard_utils import contains_secret_num
from src.keycard import Keycard


def test_keycard_contains():
    """This functions checks whether the input contains secret number or not"""
    assert contains_secret_num(
        Keycard([3, 5, -4, 8, 11, 1, -1, 6], any), 10
    ), "Test Failed: Expected contains secret num"

    assert contains_secret_num(
        Keycard([4, 6], any), 10
    ), "Test Failed: Expected contains secret num"

    assert contains_secret_num(
        Keycard([4, 6, 1, -3], any), 3
    ), "Test Failed: Expected contains secret num"

    assert contains_secret_num(
        Keycard([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], any),
        163,
    ), "Test Failed: Expected contains secret num"

    assert not contains_secret_num(
        Keycard([15], any), 15
    ), "Test Failed: Expected does not contain secret num"

    assert not contains_secret_num(
        Keycard([15], any), 14
    ), "Test Failed: Expected does not contain secret num"

    assert not contains_secret_num(
        Keycard([3, 5, -4, 8, 11, 1, -1, 6], any), 15
    ), "Test Failed: Expected does not contain secret num"

    assert not contains_secret_num(
        Keycard([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], any),
        164,
    ), "Test Failed: Expected does not contain secret num"
