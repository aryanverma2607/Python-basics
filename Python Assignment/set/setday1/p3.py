'''
3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.

'''

print("""=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================""")
visitor=set()
n=int(input("Enter number of visitor:"))
vis=[]
for i in range(n):
	id=int(input("Enter visitors id = "))
	vis.append(id)
visitor=set(vis)
print(vis)
while True:
	print("""Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit""")
	choice=(input("Enter choice : "))	
	match choice:
		case '1':
			n=int(input("Enter number visitor id to remove:"))
			visitor.add(n)
			print(visitor)
		case '2':
			n=int(input("Enter number visitor id to remove:"))
			visitor.discard(n)
			print(visitor)
		case '3':
			m=int(input("Enter visitor to check:"))
			print(m in visitor)
		case '4':
			print("All Visitor : ",visitor)
		case '5':
			print("Count : ",len(visitor))			
		case '6':
			visitor.clear()
			print("Clear data : ",visitor)
		case '7':
			print("Exit")
			break
		case __:
			print("Invalid choice")
