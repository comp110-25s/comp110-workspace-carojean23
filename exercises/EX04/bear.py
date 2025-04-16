"""File to define Bear class."""

__author__: str = "730469212"


class Bear:
    """Creates a bear that has an age and a hunger score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the bears age to be 0 and the bears hunger score to be 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """As one day passes,bear age increased by 1 and hunger score reduced by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Every time bear eats, its hunger score is increased by # of fish it ate."""
        self.hunger_score += num_fish
        return None
