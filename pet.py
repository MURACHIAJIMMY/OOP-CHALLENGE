class Pet:
    def __init__(self, name="Janel"):
        self.name = name
        self.hunger = 5  # Starting at midpoint
        self.energy = 5   # Starting at midpoint
        self.happiness = 5  # Starting at midpoint
        self.tricks = []  # For storing learned tricks
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"Janel happily munches on some food. Hunger decreased, happiness increased!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"Janel curls up and takes a cozy nap. Energy restored!")
    
    def play(self):
        if self.energy >= 2:  # Only play if there's enough energy
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"Janel wags excitedly as you play together!")
        else:
            print(f"Janel looks at you with tired eyes. Maybe time for a nap?")
    
    def get_status(self):
        print(f"\nJanel's Current Status:")
        print(f"Hunger: {'❤️' * self.hunger}{'🤍' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'⚡' * self.energy}{'🟩' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'😊' * self.happiness}{'🙂' * (10 - self.happiness)} ({self.happiness}/10)")
        
        # Personalized status messages for Janel
        if self.hunger >= 8:
            print("Janel is staring at the food bowl intensely!")
        elif self.hunger >= 5:
            print("Janel glances at the treat jar hopefully.")
        
        if self.energy <= 2:
            print("Janel is barely keeping their eyes open!")
        elif self.energy <= 5:
            print("Janel's movements are getting slower.")
        
        if self.happiness >= 8:
            print("Janel is bouncing around with joy!")
        elif self.happiness <= 2:
            print("Janel's tail droops sadly.")
    
    # Bonus methods
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"Janel mastered '{trick}'! Good job Janel!")
        else:
            print(f"Janel already knows how to {trick} (and does it perfectly)!")
    
    def show_tricks(self):
        if not self.tricks:
            print("Janel is still learning - no tricks yet but lots of potential!")
        else:
            print("Janel's impressive trick repertoire:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick.capitalize()} (performed flawlessly)")