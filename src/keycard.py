from enum import Enum


class AccessLevel(Enum):
    GREEN = "Green"
    BLUE = "Blue"
    RED = "Red"


class Keycard:
    COLOR_CODES = {
        AccessLevel.GREEN: "\033[92m",
        AccessLevel.BLUE: "\033[94m",
        AccessLevel.RED: "\033[91m",
    }
    MAX_LENGTH = 16
    MIN_LENGTH = 1

    def __init__(
        self, code: list[int], access_level: AccessLevel = AccessLevel.GREEN
    ):
        if not self.MIN_LENGTH <= len(code) <= self.MAX_LENGTH:
            raise ValueError(
                f"The code must be between {self.MIN_LENGTH} "
                f"and {self.MAX_LENGTH} integers."
            )

        if not all(isinstance(i, int) for i in code):
            raise TypeError("All elements in the code must be integers.")

        self.code = code
        self.access_level = access_level

    def __str__(self):
        reset_color = "\033[0m"

        color_code = self.COLOR_CODES.get(self.access_level, reset_color)

        return f"{color_code}[{' '.join(map(str, self.code))}]{reset_color}"

    def __repr__(self):
        return f"Keycard(code={self.code})"
