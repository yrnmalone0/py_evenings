## MAD LIBS

noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
noun_2 = input("Enter a noun(animal): ")
verb = input("Enter a verb ending with (ing): ")
noun_3 = input("Enter a noun: ")
adjective2 = input("Enter an adjective again: ")
verb2 = input("Enter a verb ending with (ing) again: ")

print("The Wild day at the Zoo")

story = f"Today, my best friend {noun} and I went to the zoo. It was a(n) {adjective} day, and the sun was shining {adverb}. First, we saw a(n) {noun_2} that was {verb} on top of a {noun_3}. It looked so {adjective2}, we couldn't stop {verb2}"

# if noun == noun_2:
#     message = "Can't proceed with same words!!"
# elif noun == noun_3:
#     message = "Can't proceed with same words, try again"
# else:
#     message = "Re-try"

# print(message)

print(story)
