class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0  # Minimum hunger level
        self.energy = 10  # Maximum energy level
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0
        self.happiness += 1
        print(f"{self.name} has eaten. Hunger level: {self.hunger}, Happiness level: {self.happiness}")

    def sleep(self):
        if self.energy <= 5:
            self.energy += 5
        else:
            self.energy = 10
        print(f"{self.name} has slept. Energy level: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
        else:
            print(f"{self.name} is too tired to play.")
        print(f"{self.name} has played. Energy level: {self.energy}, Hunger level: {self.hunger}, Happiness level: {self.happiness}")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger Level: {self.hunger}/10")
        print(f"Energy Level: {self.energy}/10")
        print(f"Happiness Level: {self.happiness}/10")
        print("--------------------------")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
