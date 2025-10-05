# File Handling with FileNotFoundError

# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

try:
    open_file = open('test.txt', 'r')
except FileNotFoundError:
    print("File not found or exist in directory")
# OR catch all other exceptions
except Exception as e:
    print(f"An error occurred: {e}")
# Run this if there are no exception
else:
    print(open_file.read())
    open_file.close()