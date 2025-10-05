# Counting Down from 5 with a Nested While Loop

# outer_count = 5

# while outer_count > 0:
#   # Outer loop controls the number of times the inner loop runs
#   inner_count = 1
#   while inner_count <= outer_count:
#     # Inner loop repeats for each outer loop iteration
#     print(inner_count, end=" ")
#     inner_count += 1
#   print()  # Move to a new line after each outer loop iteration
#   outer_count -= 1

  
# 1. The outer while loop controls how many times the inner loop runs. It starts at outer_count = 5 and keeps looping as long as outer_count is greater than 0.
# 2. The inner while loop repeats for each iteration of the outer loop. It starts at inner_count = 1 and keeps looping as long as inner_count is less than or equal to the current outer_count value.
# 3. Inside the inner loop, we print the current inner_count value and then increment it (inner_count += 1) to move on to the next number.
# 4. After each inner loop finishes, the outer loop decreases outer_count by 1, preparing for the next iteration.
# 5. Finally, a print() statement outside the inner loop moves the output to a new line after each outer loop completes, creating a countdown effect.


# Printing a Multiplication Table

# for i in range(1, 11):
#   # Outer loop iterates through rows (multiplication factors)
#   for j in range(1, 11):
#     # Inner loop iterates through columns (other factors)
#     product = i * j
#     print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
#   print()  # Move to a new line after each row



# Printing a Right Triangle of Asterisks
rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks