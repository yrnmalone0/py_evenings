import random

# Generate a secret number randomly
secret_number = random.randint(1,10)

guess_count = 0

# Prompt user to guess a number
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))

guess_count +=1

# Compare user's input with random number using a guarded match
match guess:
    ## Use an if guard to compare the of guess to the value of secret number
    case _ if guess == secret_number:  # Check if the guess is correct
        print("Congratulations, you guessed it!")

    case _ if guess > secret_number:   # Check if the guess is too high
        print("Oops, your guess is a bit high. Try again!")
    
    case _ if guess < secret_number:   # if guess is too low
        print("Nope, your guess is a bit low. Give it another shot!")

    case _:
        print("Invalid")


print(guess_count)

print(secret_number)
print(guess)