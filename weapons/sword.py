from dice.die import Die


class Sword:
    """ A class representing a sword weapon.
        Attributes:
            name (str): The name of the sword.
            die (Die): The die used to determine the attack power of the sword.
    """
    def __init__(self, name, die : Die):
        self.name = name
        self.die = die