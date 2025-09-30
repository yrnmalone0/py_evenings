# Import calculator module and use its functions to perform arithmetic operations

import calculators

#calculating estimated price
building_materials = 8
rack = 9

estimated_price = calculators.add(building_materials, rack)
print(estimated_price)

estimated_price = calculators.multiply(building_materials, rack)
print(estimated_price)

estimated_price = calculators.divide(building_materials, rack)
print(round(estimated_price))
