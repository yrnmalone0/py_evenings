#  Custom Exception

# Create a custom exception class called ValueTooHighError that inherits from the Exception class.
# Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

class ValueTooHighError(Exception):
    pass

user_input = int(input("Enter a number: "))
    

if user_input > 100:
    message = f'The value of {user_input} is higher than excepted'
    raise ValueTooHighError(message)

