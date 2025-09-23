# 1. User Input Validation
age = 0

while age < 18:
  age = int(input("Enter your age (must be 18 or older): "))

print("You are old enough to proceed.")


# 2. Guessing game
secret_number = 7

guess_count = 0
guess = 0

while guess != secret_number:
  guess_count += 1
  guess = int(input("Guess a number between 1 and 10: "))

print(f"You guessed it in {guess_count} tries!")


# 3. Iterating Until a Specific Condition
shopping_list = ["apples", "bread", "milk", "cheese"]
item_found = False

while not item_found:
  item = input("Search for an item in your list (or 'q' to quit): ")
  if item.lower() == "q":
    break  # Exit the loop if user enters 'q'
  if item in shopping_list:
    item_found = True
    print(f"{item} is on your shopping list.")
  else:
    print(f"{item} is not on your list.")