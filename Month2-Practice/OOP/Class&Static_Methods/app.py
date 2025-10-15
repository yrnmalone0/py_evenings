# Create a class Book with a class variable total_books to count the number of book instances created.
# Implement a class method display_total_books() to display the total number of books created.

class Book:
    total_books = 0

    def __init__(self, book_name):
        self.book_name = book_name

        Book.total_books += 1


    def display_total_books(self):
        return f'Total number of books is {self.total_books}'


bookA = Book("Test by Adam")
bookB = Book("Oh my gees")
bookC = Book("Hell, yes")

print(Book.display_total_books(self=Book))  
