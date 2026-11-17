'''
=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700

'''
from collections import namedtuple
print("""=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================""")

book=namedtuple("Bookdetail",["book_id","title","author","price"])
n=int(input("Enter number of books:"))
L=[]
for i in range(n):
	print()
	print(f"Enter {i+1} Book detail")
	id=input("Enter book ID : ")
	title=input("Enter Book title : ")
	author=input("Enter Author name : ")
	price=int(input("Enter Book Price : "))
	p=book(id,title,author,price)
	L.append(p)
print()
for i in L:
	print(i.book_id,i.title,i.author,i.price)
expensive=p.price
sum=0
for i in L:
	sum=sum+i.price
	if i.price>expensive:
		expensive=i.price
average=sum/n
print()
author_name=input("Enter Author name : ")
print()
print("Most Expensive Book : ")
for i in L:
	if expensive==i.price:
		print(i.book_id,i.title,i.author,i.price)
print()
print("""Average Book Price:
{}""".format(average))
print()
print(f"Books written by {author_name}")
for i in L:
	if author_name==i.author:
		print(i.book_id,i.title,i.author,i.price)

