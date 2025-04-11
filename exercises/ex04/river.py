"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish(0))
        for _ in range(0, num_bears):
            self.bears.append(Bear(0, 0))

    def check_ages(self):
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
        if len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
                self.remove_fish(3)

        return None

    def remove_fish(self, amount: int):
        if amount > len(self.fish):
            amount = len(self.fish)
        for _ in range(amount):
            self.fish.pop(0)

    def check_hunger(self):
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(bear)
        self.bears = full_bears
        return None

    def repopulate_fish(self):
        baby_fish = (len(self.fish) // 2) * 4
        for _ in range(baby_fish):
            self.fish.append(Fish(0))
        return None

    def repopulate_bears(self):
        baby_bears = len(self.bears) // 2
        for _ in range(baby_bears):
            self.bears.append(Bear(0, 3))
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
