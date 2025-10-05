## CLASSES AND OBJECTS

# Class Definition
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Methods
    def scream(self):
        return "meeaaooooo"
    
# Object Creation
male_cat = Cat("Hubby" , "Bombay")
female_cat = Cat("Chubby", "Burmese")

# Accessing object properties and class methods
print(f'{male_cat.name} is a {male_cat.breed} and it is {male_cat.scream()}ing')
print(f'{female_cat.name} is a {female_cat.breed} and it is {female_cat.scream()}ing')


class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        pass

## INHERITANCE
# inheriting the animal class
def Dog(Animal):
    def sound(self):
        return f"{self.name} the dog barks"
    

## POLYMORPHISM
animal_kingdom = [
    Dog("Wiase")
]

for animal in animal_kingdom:
    print(animal.sound())