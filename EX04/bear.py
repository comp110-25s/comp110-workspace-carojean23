"""File to define Bear class."""

<<<<<<< HEAD
__author__ = "730469212"


class Bear:
    age: int
    hunger_score: int

    def __init__(self, age, hunger_score):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        self.hunger_score += num_fish
=======
class Bear:
    
    def __init__(self):
        return None
    
    def one_day(self):
>>>>>>> 4954fadf24db33d9b42242c26251f8b16233c559
        return None
