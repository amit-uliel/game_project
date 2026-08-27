from typing import Protocol


class Die(Protocol):
    """Interface for a die"""

    def roll(self) -> int:
        ...
        