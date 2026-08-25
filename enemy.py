class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        """Reduce the enemy's health by the specified damage amount."""
        self.health -= damage
        self.health = max(self.health, 0)

    def is_alive(self):
        """Check if the enemy is still alive."""
        return self.health > 0