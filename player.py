class Player:
    """Represent a player in the game."""

    def __init__(self, name, health, level, experience):
        self.name = name
        self.health = health
        self.level = level
        self.experience = experience

    def take_damage(self, damage):
        self.health -= damage
        self.health = max(self.health, 0)  # Ensure health doesn't go below 0