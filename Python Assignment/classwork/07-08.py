#updating nested list element
'''a=[[10,20],[30,40]]
a[0].append(11)
print(a)
a[0].remove(10)
print(a)
a.pop(0)
print(a)
a=[
[1,2],
[3,4]
]
print(a)
a=[
[1,2,5],
[3,4,6],
[7,8,9]
]
print(a)
print(a[0][0])
print(a[1][2])
print(a[2][1])
'''
'''
matrix=[
[1,2,5],
[3,4,6],
[7,8,9]
]
for i in matrix:
	print(i)
for i in matrix:
	print(*i)
print("Print each element of matrix")
for i in matrix:
	for j in i:
		print(j,end=" ")
	print()
'''
'''
matrix=[
[1,2,5],
[4,3,6],
[7,8,9]
]
for i in matrix:
	for j in i:
		if j%2==0:
			print(j,end=" ")
		else:
			print(" ",end=" ")
	print()
'''
'''
row=int(input("Enter size of row: "))
col=int(input("enter size of column: "))
matrix=[]
sum1=0
for i in range(row):
	print(i,"row elements:")
	r=[]
	for i in range(col):
		r.append(int(input("Enter elements:")))	
	matrix.append(r)
	sum1 = sum1 + sum(r)
print()
print("Matrix elements are :",matrix)
for i in matrix:
	for j in i:
		print(j,end=" ")
	print()
print("Sum =",sum1)
'''
#method 2 for matrix element sum 
row=int(input("Enter size of row: "))
col=int(input("enter size of column: "))
matrix=[]
sum=0
for i in range(row):
	print(i,"row elements:")
	r=[]
	for i in range(col):
		r.append(int(input("Enter elements:")))	
	matrix.append(r)
print()
print("Matrix elements are :",matrix)
for i in matrix:
	for j in i:
		sum=sum+j
		print(j,end=" ")
	print()
print("Sum =",sum)