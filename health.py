class Health:
    """
    A class to manage the health of a character
    """
    
    def __init__(self, max_health):
        self.max_health = max_health
        self.health = max_health

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)

    def is_alive(self):
        return self.health > 0
    
    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)

    def __str__(self):
        return f"{self.health}/{self.max_health}"