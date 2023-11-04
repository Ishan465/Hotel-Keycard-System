from src.keycard_utils import contains_secret_num
from src.keycard import Keycard


def test_keycard_contains():
    assert contains_secret_num(
        Keycard([3, 5, -4, 8, 11, 1, -1, 6]), 10
    ), "Test Failed: Expected contains secret num"

    assert contains_secret_num(
        Keycard([4, 6]), 10
    ), "Test Failed: Expected contains secret num"

    assert contains_secret_num(
        Keycard([4, 6, 1, -3]), 3
    ), "Test Failed: Expected contains secret num"

    assert contains_secret_num(
        Keycard([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]), 163
    ), "Test Failed: Expected contains secret num"

    assert not contains_secret_num(
        Keycard([15]), 15
    ), "Test Failed: Expected does not contain secret num"

    assert not contains_secret_num(
        Keycard([15]), 14
    ), "Test Failed: Expected does not contain secret num"

    assert not contains_secret_num(
        Keycard([3, 5, -4, 8, 11, 1, -1, 6]), 15
    ), "Test Failed: Expected does not contain secret num"

    assert not contains_secret_num(
        Keycard([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]), 164
    ), "Test Failed: Expected does not contain secret num"
