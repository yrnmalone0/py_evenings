# fruits = ["orange", "apple", "grape","sugarcane"]

# for fruit in fruits:
#     print(fruit)

numbers = [1, 5, 3, 9]

total = 0

for number in numbers:
    # add the current number to the total variable
    total += number

print("The total value is: " + str(total))



# LOOP THROUGH A STRING
language = 'Python'

# iterate over each character in language
for x in language:
    print(x)


# BREAK STATEMENT IN LOOPS
languages = ['Swift', 'Python', 'Go', 'C++']

for lang in languages:
    if lang == 'Go':
        break
    print(lang)

# CONTINUE STATEMENT
languagesA = ['Swift', 'Python', 'Go', 'C++']

for langA in languagesA:
    if langA == 'Go':
        continue
    print(langA)