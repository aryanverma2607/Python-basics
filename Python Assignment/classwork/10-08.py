'''
row=int(input("Enter row size :"))
col=int(input("Enter column size:"))
matrix=[]
for i in range(row):
	r=[]
	for j in range(col):
		r.append(int(input("Enter element of row {} :".format(i))))
	matrix.append(r)
'''

'''
#WAP to find maximum element 
print(matrix)
max=matrix[0][0]

for i in matrix:
	for j in i:
		if j>max:
			max=j
print("Maximum number : ",max)
'''

'''
#WAP to find sum of diagonal element
sum=0
for i in range(row):
	for j in range(col):
		if i==j:
			sum=sum+matrix[i][j]
print("Diagonal Sum = ",sum)
sum=0
for i in range(row):
	sum=sum+matrix[i][i]
print("Diagonal Sum = ",sum)
'''

#WAP to count even number in matrix
'''
count=0
for i in range(row):
	for j in range(col):
		if matrix[i][j]%2==0:
			count=count+1
print(count)
'''

'''
#WAP to program to search element in matrix and display index
K=int(input("enter element to search:"))
for i in range(row):
	for j in range(col):
		if matrix[i][j]==K:
			print("{} Found at {} {}".format(K,i,j))
else:
	print("No Element found")
'''


#WAP to add element of two matrix
'''
row=int(input("Enter row size :"))
col=int(input("Enter column size:"))

row1=int(input("Enter 1 row size :"))
col1=int(input("Enter 2 column size:"))

if row1==row and col==col1:
	matrix=[]
	for i in range(row):
		r=[]
		for j in range(col):
			r.append(int(input("Enter element {} of Matrix 1 :".format(i))))
		matrix.append(r)
	matrix1=[]
	for i in range(row1):
		r=[]
		for j in range(col1):
			r.append(int(input("Enter element {} of matrix 2 :".format(i))))
		matrix1.append(r)

	# new addition matrix
	c=[]
	for i in range(len(matrix)):
		new=[]
		for j in range(len(matrix1)):
			new.append(matrix[i][j]+matrix1[i][j])
		c.append(new)
	print(*c)
else:
	print("Matrix Size not equal")
'''
#WAP to Multiply two matrix


# number of column of matrix 1 = number of row of matrix2


row=int(input("Enter row size of first matrix:"))
col=int(input("Enter column size of first matrix:"))

row1=int(input("Enter row size of second matrix :"))
col1=int(input("Enter column size of second matrix:"))

if col==row1:

	print("Elements of first matrix")
	matrix=[]
	for i in range(row):
		r=[]
		for j in range(col):
			r.append(int(input("Enter element {} of Matrix 1 :".format(i))))
		matrix.append(r)
	print()
	for r in matrix:
		print(*r)
	print("Elements of Second matrix")
	matrix1=[]
	for i in range(row1):
		r=[]
		for j in range(col1):
			r.append(int(input("Enter element {} of matrix 2 :".format(i))))
		matrix1.append(r)
	print()
	for r in matrix1:
		print(*r)
	print()
	result=[]
	for i in range(row):
		r=[]
		for j in range(col1):
			r.append(0)
		result.append(r)
	for i in range(row):
		for j in range(col1):
			for k in range(col):
				result[i][j]=result[i][j]+matrix[i][k]*matrix1[k][j]
	print(result)
	for r in result:
		print(*r)
		
else:
	print("multipliction not possible")
	
