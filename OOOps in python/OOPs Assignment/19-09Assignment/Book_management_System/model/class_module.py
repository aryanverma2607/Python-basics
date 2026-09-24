'''============================================================
ASSIGNMENT 5 – BOOK MANAGEMENT SYSTEM
=====================================

Create a Book class inside:

models/book.py

ATTRIBUTES:

* book_id
* book_name
* author
* price

TASKS:

1. Take details of 5 books from the user.
2. Create Book objects.
3. Store all Book objects in a list.
4. Display all books.
5. Search a book using Book Id.
6. Display all books written by a particular author.
7. Display books whose price is greater than 500.
8. Find the most expensive book.
9. Calculate average price of all books.

SAMPLE INPUT:

101 Java Programming James 650
102 Python Basics Mark 550
103 MySQL Guide John 450
104 Advanced Java James 800
105 DSA in Python Robert 700

EXPECTED OUTPUT:

All Books:
101 Java Programming James 650
102 Python Basics Mark 550
103 MySQL Guide John 450
104 Advanced Java James 800
105 DSA in Python Robert 700

Books by James:
101 Java Programming 650
104 Advanced Java 800

Books with price greater than 500:
Java Programming
Python Basics
Advanced Java
DSA in Python

Most Expensive Book:
Advanced Java = 800

Average Price:
630
'''
books=[]
class book:
    def __init__(self):
        self.id=int(input("Enter Book ID:"))
        self.name=input("Enter Book Name:")
        self.author=input("Enter Author Name:")
        self.price=int(input("Enter Book Price:"))
        books.append(self)

    def display(self):
        print("\nAll Books:")
        for i in books:
            print(i.id,i.name,i.author,i.price)

    def found(self):
        self.id_=int(input('\nEnter Book ID:'))
        for i in books:
            if self.id==i.id:
                print(i.id,i.name,i.author,i.price)
                break
        else:
            print('Book ID not found')

    def found_author(self):
        self.author_=input("\nEnter Author name:")
        for i in books:
            if self.author_==i.author:
                print(i.id,i.name,i.author,i.price)
                break
        else:
            print("Author not found")

    def greater_than500(self):
        print("\nBook Price Greater than 500:")
        for i in books:
            if i.price>500:
                print(i.id,i.name,i.author,i.price)

    def expensive(self):
        x=0
        print("\nMost Expensive Book:")
        for i in books:
            if i.price>x:
                x=i.price
        for i in books:
            if i.price==x:
                print(i.id,i.name,i.author,i.price)

    def average(self):
        total=0
        print("\nAverage Price:")
        for i in books:
            total=total+i.price
        average=total/len(books)
        print(average)
