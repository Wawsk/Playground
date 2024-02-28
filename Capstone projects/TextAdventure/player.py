class Player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.attack = 10
        self.defense = 5

    def choose_name(self):
        self.name = input("Enter your name: ")

    def choose_class(self):
        print("Choose your class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            self.attack += 5
            self.defense += 5
        elif choice == "2":
            self.attack += 10
        elif choice == "3":
            self.defense += 10
        else:
            print("Invalid choice. Defaulting to Warrior.")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.take_damage(damage)
        print(f"You attack the {enemy.name} for {damage} damage!")