import random
import player
import world

class Game:
    def __init__(self):
        self.player = player.Player()
        self.world = world.World()

    def start(self):
        print("Welcome to the Text Adventure Game!")
        print("Your journey begins...")
        self.player.choose_name()
        self.player.choose_class()
        self.player.show_stats()
        self.world.explore(self.player)


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount

    def attack_player(self, player):
        damage = random.randint(1, self.attack)
        player.take_damage(damage)
        print(f"The {self.name} attacks you for {damage} damage!")

class Boss(Enemy):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def attack_player(self, player):
        damage = random.randint(1, self.attack + 10)
        player.take_damage(damage)
        print(f"The {self.name} attacks you for {damage} damage!")


class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def talk(self):
        print(f"{self.name}: {self.dialogue}")


class Event:
    def __init__(self, description):
        self.description = description

    def trigger(self, player):
        print(self.description)
        # Implement specific event logic here


class World:
    def __init__(self):
        self.events = [
            Event("You find a treasure chest."),
            Event("You encounter a friendly NPC."),
            Event("A wild enemy appears!")
        ]

    def explore(self, player):
        while True:
            choice = input("Do you want to explore? (yes/no): ").lower()
            if choice == "yes":
                event = random.choice(self.events)
                event.trigger(player)
                if isinstance(event, Event) and "enemy" in event.description:
                    enemy = Enemy("Goblin", 20, 5)  # Example enemy
                    self.battle(player, enemy)
            else:
                print("You decide to stop exploring.")
                break

    def battle(self, player, enemy):
        print(f"A wild {enemy.name} appears!")
        while player.is_alive() and enemy.is_alive():
            player.attack(enemy)
            if enemy.is_alive():
                enemy.attack_player(player)
        if player.is_alive():
            print("You defeated the enemy!")
        else:
            print("Game over! You were defeated.")


class BossRoom(Event):
    def __init__(self):
        super().__init__("You've entered the boss room!")

    def trigger(self, player):
        print(self.description)
        boss = Boss("Dragon", 100, 20)  # Example boss
        player.attack(boss)
        if boss.is_alive():
            boss.attack_player(player)
        if player.is_alive():
            print("Congratulations! You defeated the dragon and won the game!")
        else:
            print("Game over! You were defeated by the dragon.")


