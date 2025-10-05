#  Handling ZeroDivisionError

# Write a program that takes two numbers as input from the user and divides the first number by the second number.
# Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

try:
    result = first_number / second_number
    print(f"The result of {first_number} and {second_number} is {result}")
except ZeroDivisionError:
    print(f"cannot divide {first_number} by zero(0)")