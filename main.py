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

for book in library.list_books():
    print(book)



#Example 2

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)

    def listed_animals(self):
        return [f"{animal.cow} and {animal.goat}" for animal in self.animals]


class Animal:
    def __init__(self, cow, goat):
        self.cow = cow
        self.goat = goat


farm = Farm("The Great Breeder Ranch")

batch1 = Animal("cowsy1", "goatmatata1")
batch2 = Animal("cowseycow", "goatie")
batch3 = Animal("cowwow", "goatedbull")

farm.add_animal(batch1)
farm.add_animal(batch2)
farm.add_animal(batch3)

print(farm.name)

for animal in farm.listed_animals():
    print(animal)


#Example 3

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def student_list(self):
        return [f"{student.name} scored {student.grade}" for student in self.students]


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade 
        

school = School("The University of Titans, CA County")

stud1 = Student("Caden", 98)
stud2 = Student("Frank", 90)
stud3 = Student("Ashley", 92)
stud4 = Student("Rosey", 93)