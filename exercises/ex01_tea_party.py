"""My second coding exercise to calculate the cost of a new party based on the number of guests"""

__author__: str = "730469212"


def main_planner(guests: int) -> None:
    """Entrypoint of my program to ask for guests for tea party calculations"""
    print("A Cozy Tea Party For", guests, "People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """the number teabags needed for all guests attending the party"""
    return people * 2


def treats(people: int) -> int:
    """The number of treats needed for all guests attending the party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates total cost of supplies needed for tea party"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))