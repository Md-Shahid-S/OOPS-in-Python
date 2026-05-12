# super() — the right way to call parent methods

class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        print(f"Animal __init__ called for {name}")

class Pet(Animal):
    def __init__(self, name: str, species: str, owner: str):
        super().__init__(name, species)   # ✅ Correct — calls Animal.__init__
        self.owner = owner
        print(f"Pet __init__ called for {name}")

class Dog(Pet):
    def __init__(self, name: str, owner: str, breed: str):
        super().__init__(name, "Canis lupus", owner)  # ✅ Calls Pet.__init__
        self.breed = breed
        print(f"Dog __init__ called for {name}")


dog = Dog("Bruno", "Affu", "Labrador")
# Animal __init__ called for Bruno    ← chain goes all the way up
# Pet __init__ called for Bruno
# Dog __init__ called for Bruno

print(dog.name)     # Bruno     ← set by Animal.__init__
print(dog.owner)    # Affu      ← set by Pet.__init__
print(dog.breed)    # Labrador  ← set by Dog.__init__