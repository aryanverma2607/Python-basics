'''
8.
MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit
Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4
'''
while True:
	print("""Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit""")
	choice=input("Enter Your Choice : ")
	match choice:
		case '1':
			row=int(input("Enter Row size : "))
			column=int(input("Enter Column size : "))
			matrix=[]
			for i in range(row):
				r=[]
				for j in range(column):
					a=int(input("Enter Row {} element : ".format(i+1)))
					r.append(a)
				matrix.append(r)
			count=0
			for i in range(column):
				for j in range(row):
					if j>i and matrix[i][j]%2==0:
						count+=1 
			print(count)
				
		case '2':
			row=int(input("Enter Row size : "))
			column=int(input("Enter Column size : "))
			matrix=[]
			for i in range(row):
				r=[]
				for j in range(column):
					a=int(input(f"Enter Row {i+1} element : "))
					r.append(a)
				matrix.append(r)
			count=0
			for i in range(row):
				for j in range(column):
					if i>j and matrix[i][j]%2!=0:
						count+=1 
			print(count)
		case '3':
			row=int(input("Enter Row size : "))
			column=int(input("Enter Column size : "))
			matrix=[]
			for i in range(row):
				r=[]
				for j in range(column):
					a=int(input(f"Enter Row {i+1} element : "))
					r.append(a)
				matrix.append(r)
			for i in matrix:
				print(*i)
			new=[]
			for i in range(len(matrix)):
				n=matrix[0][i]
				new.append(n)
			for k in range(len(matrix)):
				n1=matrix[k][column-1]
				if n1 not in new:
					new.append(n1)
			for j in range(len(matrix)):
				n2=matrix[row-1][column-1-j]
				if n2 not in new:
					new.append(n2)
			for x in range(len(matrix)):
				n3=matrix[row-1-x][0]
				if n3 not in new:
					new.append(n3)
			print("Boundary Element:")
			for i in new:
				print(i,end=" ")
			print()
		case '4':
			print("Exit")
			break
		case __:
			print("Invalid choice")