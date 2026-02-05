#Aggregation => relationship where one object (the whole) contains references to one or more Independent objects (the parts)


class Library:
    def __init__(self, name):
        self.name = name
        




class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

library = Library("Andrew Carnagie Library - MIT Research Center")

book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("Pride and Prejudice", "Jane Austen")
book3 = Book("The Catcher in the Rye", "J. D. Salinger")
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald")