'''
QUESTION 3: LIBRARY BOOK RECORD ANALYSIS(3 marks)

A library wants to maintain and analyze its book records using NamedTuple.

Each book contains the following information:

Fields:
book_id, title, author, price

Requirements:
Read N book records from the user and store them in a list of NamedTuple.
Display all book details.
Find and display the most expensive book.
Find and display the cheapest book.
Calculate and display the average price of all books.
Display all books whose price is greater than the average book price.
Test Case

'''
from collections import namedtuple
book=namedtuple("Books",["book_id","title","author","price"])

books=[]
N=int(input("Enter number of books: "))
for i in range(N):
    book_id=input("Enter book id: ")
    title=input("Enter title: ")
    author=input("Enter author name: ")
    price=int(input("Enter book price: "))
    b=book(book_id,title,author,price)
    books.append(b)

print("\nAll book details:")
for i in books:
    print(i.book_id,i.title,i.author,i.price)
highest=0
lowest=1000000000000
sum=0
for i in books:
    if i.price>highest:
       highest=i.price
    if i.price<lowest:
       lowest=i.price
    sum=sum+i.price
for i in books:
     if i.price==highest:
        print("\nExpensive Book: ",i.book_id,i.title,i.author,i.price)
     if i.price==lowest:
        print("\nCheapest Book: ",i.book_id,i.title,i.author,i.price)
a=sum/N
print("\nAverage of book = ",a)

print("\nBooks Above Average:")
for i in books:
    if i.price>a:
          print(i.book_id,i.title,i.author,i.price)

