from dice import roll_dice
from player import Player


def main():
    # Create a new player
    player_name = input("Enter your player's name: ")
    player = Player(name=player_name, health=100, level=1, experience=0)

    print(f"Welcome, {player.name}! Your journey begins now.")
    print(f"Health: {player.health}, Level: {player.level}, Experience: {player.experience}")

    # Simulate taking damage
    damage = roll_dice(10)  # Roll a 10-sided dice for damage
    player.take_damage(damage)
    print(f"{player.name} took {damage} damage. Current health: {player.health}")