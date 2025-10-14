# Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
# Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods

class Bird:

    def fly(self):
        return f'Flying.....'
    
class Mammal:

    def run(self):
        return f'Running.....'
    
class Bat(Bird, Mammal):
    pass

bat = Bat()
print(bat.fly())
print(bat.run())