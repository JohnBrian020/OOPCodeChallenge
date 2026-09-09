class Pet:
    def __init__(self, name, animal_type):
    # Create the attributes here
        self.name = name
        self.animal_type = animal_type
        self.hunger = 5
        self.energy = 5

    def feed(self):
    # Reduce hunger
        if self.hunger > 5:
            print(f" {self.name} is not hungry right now.")
        else:
            self.hunger -= 1
            print(f"{self.name} enjoyed the food!")
            print(f"Hunger Level: {self.hunger}")
            
    def play(self):
    # Increase hunger and decrease energy
        if self.energy <= 1:
            print(f"{self.name} is too tired to play.")
        else:
            self.energy -= 1
            print(f"{self.name} has an Energy Level: {self.energy} and had fun playing!")

        if self.hunger <= 5:
            self.hunger += 1
            print(f"Hunger Level: {self.hunger},")
            print(f"{self.name} has an Hunger Level: {self.hunger} and is too hungry to play!")
    def status(self):
    # Display the pet's information
        print(f"{self.name}'s status:")
        print(f"Animal type: {self.animal_type}")
        print(f"Hunger level: {self.hunger}")
        print(f"Energy level: {self.energy}")
            
pet1 = Pet("Milo", "Dog")
pet2 = Pet("Luna", "Cat")

pet1.feed()
pet1.play()
pet1.status()
