from typing import Protocol


class Rollable(Protocol):
    """A protocol for objects that can be rolled to produce a random integer value."""

    def roll(self) -> int:
        ...
        