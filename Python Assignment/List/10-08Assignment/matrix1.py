'''
1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

'''
print("""=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================""")

while True:
	print("""1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit""")
	choice=int(input("Enter Your Choice:"))
	match choice:
		case 1:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			r2=int(input("Enter Row Size of Matrix B:"))
			c2=int(input("Enter Column Size of Matrix B:"))
			l1=[]
			l2=[]
			if r1==r2 and c1==c2:
				for i in range(r1):
					r=[]
					for j in range(c1):
						r.append(int(input(f"Enter {j} Element of {i} row:")))
					l1.append(r)
				for i in l1:
					print(*i)
				for i in range(r2):
					r=[]
					for j in range(c2):
						r.append(int(input(f"Enter {j} Element of {i} row:")))
					l2.append(r)
				for i in l2:
					print(*i)
				new=[]
				for i in range(len(l1)):
					n=[]
					for j in range(len(l1[i])):
						n.append(l1[i][j]+l2[i][j])
					new.append(n)
				print("Resultant Matrix:")
				for i in new:
					print(*i)
			else:
				print("Matrix Dimension is not equal")
		case 2:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			r2=int(input("Enter Row Size of Matrix B:"))
			c2=int(input("Enter Column Size of Matrix B:"))
			l1=[]
			l2=[]
			if r1==r2 and c1==c2:
				for i in range(r1):
					r=[]
					for j in range(c1):
						r.append(int(input(f"Enter {j} Element of {i} row:")))
					l1.append(r)
				for i in l1:
					print(*i)
				for i in range(r2):
					r=[]
					for j in range(c2):
						r.append(int(input(f"Enter {j} Element of {i} row:")))
					l2.append(r)
				for i in l2:
					print(*i)
				new=[]
				for i in range(len(l1)):
					n=[]
					for j in range(l1[i]):
						n.append(l2[i][j]-l1[i][j])
					new.append(n)
				print("Resultant Matrix:")
				for i in new:
					print(*i)
			else:
				print("Matrix Dimension is not equal")
		case 3:
			r1=int(input("Enter Row Size of Matrix A:"))
			c1=int(input("Enter Column Size of Matrix A:"))
			r2=int(input("Enter Row Size of Matrix B:"))
			c2=int(input("Enter Column Size of Matrix B:"))		
			l1=[]
			l2=[]
			if r1==r1 and c1==c2:
				for i in range(r1):
					r=[]
					for j in range(c1):
						r.append(int(input(f"Enter {j} Element of {i} row:")))
					l1.append(r)
				for i in l1:
					print(*i)
				for i in range(r2):
					r=[]
					for j in range(c2):
						r.append(int(input(f"Enter {j} Element of {i} row:")))
					l2.append(r)
				for i in l2:
					print(*i)
				for i in range(len(l1)):
					for j in range(len(l2)):
						if l1[i][j]!=l2[i][j]:
							print("Matrix Not Equal")
							break

				else:
					print("Matrix are equal")
		case 4:
			print("Thank You for Using Matrix Operations Management System")
			break
		
	