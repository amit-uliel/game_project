import random

from characters.enemy import Enemy
from characters.player import Player
from dice.simple_die import SimpleDie
from health import Health
from weapons.sword import Sword


def main():
    # Create new dice
    five_sided_die = SimpleDie(rng=random.Random(), sides=5)
    ten_sided_die = SimpleDie(rng=random.Random(), sides=10)

    # Create new weapons
    wooden_sword = Sword(name="Wooden Sword", damage=five_sided_die)
    iron_sword = Sword(name="Iron Sword", damage=ten_sided_die)

    # Create health object for the player
    player_health = Health(max_health=100)
    enemy_health = Health(max_health=50)

    # Create a new player
    player = Player(name="Hero", health=player_health, weapon=iron_sword)

    # Create a new enemy
    enemy = Enemy(name="Goblin", health=enemy_health, weapon=wooden_sword)

    print(f"Welcome, {player.name}! Your journey begins now.")
    print(f"Health: {player.health} | Weapon: {player.weapon.name}")
    print(f"Enemy: {enemy.name}, Health: {enemy.health} | Weapon: {enemy.weapon.name}")

    # Simulate taking damage
    enemy_damage = enemy.weapon.damage.roll()
    print(f"{enemy.name} attacks {player.name} with {enemy.weapon.name} for {enemy_damage} damage!")
    player.health.take_damage(enemy_damage)
    print(f"{player.name} took {enemy_damage} damage. Current health: {player.health}")
    
    print()

    player_damage = player.weapon.damage.roll()
    print(f"{player.name} attacks {enemy.name} with {player.weapon.name} for {player_damage} damage!")
    enemy.health.take_damage(player_damage)
    print(f"{enemy.name} took {player_damage} damage. Current health: {enemy.health}")

main()