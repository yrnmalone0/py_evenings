soft_drinks = 250
cookies = 105
baggie_jeans = 5000

# Ask user to input the quantity for each item they want to buy
item_quantityA = int(input("Enter quantity for soft drinks: "))
item_quantityB = int(input("Enter quantity for cookies: "))
item_quantityC = int(input("Enter quantity for baggie jeans: "))

# Calculate total cost by multiplying the quantity by the price for each item 
total_costA = item_quantityA * soft_drinks
total_costB = item_quantityB * cookies
total_costC = item_quantityC * baggie_jeans

# summing them up
results = (total_costA + total_costB + total_costC)

print(results)