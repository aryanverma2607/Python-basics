'''Question 6: Library Book Management System
A library wants to maintain information about books. The librarian should be able to:

View book details.
Issue the book to a student.
Return the book.

Requirements
Create a class named Book with the following attributes:
book_id
title
author
status (Initially "Available")

Initialize the values using a constructor.
Create the following methods:
display_details() → Displays all book information.
issue_book() → Changes the status to "Issued".
return_book() → Changes the status to "Available".
Sample Input
Enter Book ID : B101
Enter Book Title : Python Programming
Enter Author Name : John Smith
Sample Output
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available

Book issued successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Issued

Book returned successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available
'''
class book:
    def __init__(self,id,title,author,status):
        self.id=id
        self.title=title
        self.author=author
        self.status=status
    def display_details(self):
        print(f"""\n------ Book Details ------
Book ID     : {self.id}
Title       : {self.title}
Author      : {self.author}
Status      : {self.status}""")
    def issue_book(self):
        self.status="Issued"
        print(f"""\nBook issued successfully.

------ Book Details ------
Book ID     : {self.id}
Title       : {self.title}
Author      : {self.author}
Status      : {self.status}""")


    def return_book(self):
        self.status="Available"
        print(f"""\nBook Returned successfully.

------ Book Details ------
Book ID     : {self.id}
Title       : {self.title}
Author      : {self.author}
Status      : {self.status}""")


b=book("B1o1","Python Programming","John Smith","Available")
b.display_details()
b.issue_book()
b.return_book()