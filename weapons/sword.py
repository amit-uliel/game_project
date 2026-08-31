from dice.rollable import Rollable


class Sword:
    """ A class representing a sword weapon.
        Attributes:
            name (str): The name of the sword.
            die (Rollable): The die used to determine the attack power of the sword.
    """
    def __init__(self, name, damage : Rollable):
        self.name = name
        self.damage = damage