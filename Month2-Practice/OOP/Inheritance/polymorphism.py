# Create classes Dog, Cat, and Bird, each with a method make_sound().
# Implement different behaviors for make_sound() in each class.
# Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.

class Dog:
    def make_sound(self):
        return("Wowo wo...ooo")

class Cat:
    def make_sound(self):
        return("meoowwwww...")

class Bird:
    def make_sound(self):
        return("Kirzaaazzz .......")
    

def let_them_speak(animals):
    animals = [Dog(), Cat(), Bird()]
    
    for animal_type in animals:
        print(animal_type.make_sound())

let_them_speak([])

