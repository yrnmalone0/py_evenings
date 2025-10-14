## Create a base class Animal with methods like eat and sleep.
## Create a subclass Dog that inherits from Animal and adds a method bark.
## Create instances of both classes and demonstrate method inheritance.

class Animal:

    def __init__(self):
        pass

    def eat(self):
        return f'Eating......'
    
    def sleep(self):
        return f'Sleeping......'

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        return f'Wowo wo wo!!!'
    
animalA = Animal()
dogB = Dog()

print(animalA.eat())
print(animalA.sleep())
print(dogB.eat())
print(dogB.sleep()) 
print(dogB.bark())