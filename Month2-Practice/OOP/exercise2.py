## Create a Book class with attributes like title, author, and pages.

## Implement both __str__ and __repr__ magic methods to provide different string representations of the book object.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author} has {self.pages} pages.'
    
    def __repr__(self):
        return f'Book{self.title}, {self.author}, {self.pages}'
    
bookA = Book("AA","Kwame","PG.1-2")
bookB = Book("BB","Ama","PG.3-4")


print(bookA.__str__())
print(bookA.__repr__())

print(bookB.__repr__())
print(bookB.__str__())