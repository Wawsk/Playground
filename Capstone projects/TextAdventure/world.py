from game import BossRoom

class World:
    def __init__(self):
        self.events = [
            BossRoom(),
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
