## PYTHON LISTS ##

# Allows duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(thislist[-1])

# List length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print(type(thislist))

# Check if Item Exists
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
