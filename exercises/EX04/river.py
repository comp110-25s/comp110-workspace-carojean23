"""File to define River class."""

__author__: str = "730469212"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Creates a river with bears, fish, and passing days."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of the organisms and if too old, they removed from river."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """If there is ample fish, a bear will eat 3 fish and remove them from river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)

        return None

    def remove_fish(self, amount: int):
        """Removes fish after they die naturally or are eaten."""
        if amount > len(self.fish):
            amount = len(self.fish)
        for _ in range(amount):
            self.fish.pop(0)

    def check_hunger(self):
        """Removes bears from river if they are too hungry to survive."""
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(bear)
        self.bears = full_bears
        return None

    def repopulate_fish(self):
        """Adds 4 fish to the river for every two fish that reproduce."""
        baby_fish = (len(self.fish) // 2) * 4
        for _ in range(baby_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Adds 1 bear to the river for every two bears that reproduce."""
        baby_bears = len(self.bears) // 2
        for _ in range(baby_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Creates an output display to show the current state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates a week of life in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
