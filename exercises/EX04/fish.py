"""File to define Fish class."""

__author__ = "730469212"


class Fish:
    age: int

    def __init__(self, age):
        self.age = 0
        return None

    def one_day(self):
        self.age += 1
        return None
