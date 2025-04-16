"""File to define Fish class."""

__author__: str = "730469212"


class Fish:
    """Creates a fish that has an age."""

    age: int

    def __init__(self):
        """Initializes the fish to have an age."""
        self.age = 0
        return None

    def one_day(self):
        """As one day passes the fish increases in age by 1."""
        self.age += 1
        return None
