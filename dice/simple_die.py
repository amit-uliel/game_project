class SimpleDie:
    """ A simple die class that represents a die with a specified number of sides."""
    def __init__(self, rng, sides):
        self.sides = sides
        self.rng = rng

    # Roll the die and return a random number between 1 and the number of sides.
    def roll(self):
        return self.rng.randint(1, self.sides)