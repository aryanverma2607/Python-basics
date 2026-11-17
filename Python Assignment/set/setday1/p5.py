'''
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.
'''
print("""=========================================
LIBRARY ISBN MANAGER
=========================================""")


books=set()
n=int(input("Enter number of books:"))
number=[]
for i in range(n):
	isbn=int(input("Enter ISBN number:"))
	number.append(isbn)
books=set(number)
while True:
	print("""Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit""")
	choice=(input("Enter choice : "))	
	match choice:
		case '1':
			n=int(input("Enter ISBN number to add:"))
			books.add(n)
			print(books)
		case '2':
			n=int(input("Enter ISBN number to remove:"))
			books.discard(n)
			print(books)
		case '3':
			n=int(input("Enter ISBN number to search:"))
			print(n in books)
		case '4':
			print("ISBN number : ",books)
		case '5':
			print("Books count : ",len(books))
		case '6':
			print("Exit")
			break
		case __:
			print("Invalid choice")
				
