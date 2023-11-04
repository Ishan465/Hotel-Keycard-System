from src.keycard_utils import duplicate
from src.keycard import Keycard, AccessLevel


def test_duplicate_keycard():
    original_keycard = Keycard([1, 2, 3, 4], AccessLevel.BLUE)
    duplicated_keycard = duplicate(original_keycard)

    assert (
        original_keycard.code == duplicated_keycard.code
    ), "Test Failed: Expected codes to be equal"

    assert (
        original_keycard.access_level == duplicated_keycard.access_level
    ), "Test Failed: Expected access levels to be equal"

    # Modify the original keycard's code to ensure that the duplicated
    # keycard's code is a deep copy
    original_keycard.code[0] = 9

    assert (
        original_keycard.code != duplicated_keycard.code
    ), "Test Failed: Expected codes to be different"
