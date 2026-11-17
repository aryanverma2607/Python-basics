'''
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

'''
print("""=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================
""")
while True:
	print("""1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit""")
	choice=int(input("Entr number : "))
	match choice:
		case 1:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			A=[]
			for a in range(r1):
				row=[]
				for b in range(c1):
					row.append(int(input("Enter {} Element of row {}:".format(b+1,a))))
				A.append(row)
			for c in A:
				print(*c)
			print("Diagonal Element = ",end=" ")
			for i in range(r1):
				for j in range(c1):
					if i==j:
						print(A[i][j],end=" ")
			print()
					
		case 2:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			A=[]
			for a in range(r1):
				row=[]
				for b in range(c1):
					row.append(int(input("Enter {} Element of row {}:".format(b+1,a))))
				A.append(row)
			for c in A:
				print(*c)
			print("Secondary Diagonal Element = ",end=" ")
			for i in range(r1):
				for j in range(c1-1,-1,-1):
					print(A[i][j],end=" ")
					c1-=1
					break
			print()
		case 3:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			A=[]
			for a in range(r1):
				row=[]
				for b in range(c1):
					row.append(int(input("Enter {} Element of row {}:".format(b+1,a))))
				A.append(row)
			for c in A:
				print(*c)
			sd=0
			for i in range(r1):
				for j in range(c1):
					if i==j:
						sd=sd+A[i][j]
			ssd=0
			for i in range(r1):
				for j in range(c1-1,-1,-1):
					print(A[i][j],end=" ")
					c1-=1
					break
		case 4:
			print("Thank You for Using Matrix Quality Check System")
			break