# Multilevel Inheritance in Python

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display(self):
        print(f"Name: {self.name}\nSpecies: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")   
        self.breed = breed

    def display(self):
        super().display()   
        print(f"Breed: {self.breed}")

class Labra(Dog):
    def __init__(self, name, colour):
        super().__init__(name, breed="Labra")   
        self.colour = colour

    def display(self):
        super().display()  
        print(f"Colour: {self.colour}")

# Object creation
x = Labra("Leo", "White")
x.display()