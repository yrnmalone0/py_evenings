class Catalogue:
    def __init__(self, name: str, price: float, quantity=0):

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

catalogue1 = Catalogue("Channel", 22.9, 2)
catalogue2 = Catalogue("Gucci", 340.0, 3)

print(catalogue1.calculate_total())
print(catalogue2.calculate_total())
