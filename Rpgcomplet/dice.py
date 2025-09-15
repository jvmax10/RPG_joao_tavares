import random

class Dice:
    @staticmethod
    def roll_dice(num, sides):
        return sum(random.randint(1, sides) for _ in range(num))

    @staticmethod
    def roll_3d6():
        return Dice.roll_dice(3, 6)

    @staticmethod
    def roll_4d6_drop_lowest():
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)