class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Location:
    def __init__(self, name):
        self.name = name
        self.treasures = []

    def add_treasure(self, treasure):
        self.treasures.append(treasure)

    def show_treasures(self):
        print(f"Treasures in {self.name}:")
        for treasure in self.treasures:
            print(f"- {treasure.name}")

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.score = 0

    def collect(self, treasure):
        self.inventory.append(treasure)
        self.score += treasure.value

    def show_inventory(self):
        print(f"{self.name}'s inventory:")
        for item in self.inventory:
            print(f"- {item.name}: {item.value} points")
        print(f"Total score: {self.score} points")
        
gold_coin = Treasure("Gold Coin", 100)
diamond = Treasure("Diamond", 500)
ancient_map = Treasure("Ancient Map", 250)

cave = Location("Dark Cave")
beach = Location("Hidden Beach")

cave.add_treasure(gold_coin)
cave.add_treasure(diamond)
beach.add_treasure(ancient_map)

player1 = Player("Amina")

cave.show_treasures()

player1.collect(gold_coin)
player1.collect(diamond)

player1.show_inventory()