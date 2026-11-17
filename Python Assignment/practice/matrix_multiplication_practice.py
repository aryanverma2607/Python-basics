'''
problem 2:-   3 marks

Matrix Multiplication

Write a Python program to read two matrices from the user and perform matrix multiplication.

Before multiplying the matrices, check whether multiplication is possible. Matrix multiplication is possible only if
the number of columns in the first matrix is equal to the number of rows in the second matrix.

Requirements
Read the number of rows and columns for the first matrix.
Read all the elements of the first matrix from the user.
Read the number of rows and columns for the second matrix.
Read all the elements of the second matrix from the user.
Check whether matrix multiplication is possible.
If possible, multiply the matrices using nested loops.
Display the resulting matrix.

If multiplication is not possible, display:

Matrix multiplication is not possible.

'''
r1=int(input("Enter Size of row1:"))
c1=int(input("Enter Size of Column1:"))
r2=int(input("Enter Size of row2:"))
c2=int(input("Enter Size of column2:"))
m1=[]
m2=[]
for i in range(r1):
    r=[]
    for j in range(c1):
        a=int(input("Enter element {} of row {} matrix 1 :".format(j+1,i+1)))
        r.append(a)
    m1.append(r)
for i in range(r2):
    r=[]
    for j in range(c2):
        a=int(input("Enter element {} of row {} matrix2 :".format(j+1,i+1)))
        r.append(a)
    m2.append(r)

result=[]
for i in range(r1):
     r=[]
     for j in range(c2):
         r.append(0)
     result.append(r)

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j]=result[i][j]+m1[i][k]*m2[k][j]


for i in result:
    print(*i)




       