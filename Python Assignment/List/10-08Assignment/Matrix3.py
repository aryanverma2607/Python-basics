'''

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

'''

print("""=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================""")

while True:
	print("""1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
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
			for i in range(len(A)):
				count=0
				for j in A[i]:
					num=j
					temp=num
					p=len(str(num))
					sum=0
					while num>0:
						r=num%10
						sum=sum+r**p
						num=num//10
					if sum==temp:
						count+=1
				print(F"Row {i} Armstrong number = {count}")
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
			for i in range(c1):
				count=0
				for j in range(r1):
					num=A[j][i]
					temp=num
					rev=0
					while num>0:
						r=num%10
						rev=rev*10+r
						num=num//10
					if rev==temp:
						count+=1
				print(F"Column {i} Palindrome count = {count}")	
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
			for i in range(r1):
				sum1=sum(A[i])
				print("Average of row {} = {}".format(i,sum1/c1))
		case 4:
			print("Thank You for Using Matrix Quality Check System")
			break			