#Aggregation => relationship where one object (the whole) contains references to one or more Independent objects (the parts)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
        




class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

library = Library("Andrew Carnagie Library - MIT Research Center")

book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("Pride and Prejudice", "Jane Austen")
book3 = Book("The Catcher in the Rye", "J. D. Salinger")
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

print(library.name)