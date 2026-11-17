'''
QNO 1: Matrix Transpose & Diagonal Transformation(3.5 marks)

Write a Python program that accepts an N × N square matrix from the user.

The program must:

Display the original matrix.
Find and display the Main Diagonal elements.
Find and display the Secondary Diagonal elements.
Create the transpose of the matrix.
In the transposed matrix, swap each Main Diagonal element with the corresponding Secondary Diagonal element.
Display the final matrix.
The original matrix must not be modified.
Input
Enter the size of matrix: 4

Enter matrix elements:
10 20 30 40
50 60 70 80
90 15 25 35
45 55 65 75
Expected Output
Original Matrix:
10 20 30 40
50 60 70 80
90 15 25 35
45 55 65 75

Main Diagonal Elements:
10 60 25 75

Secondary Diagonal Elements:
40 70 15 45

Transpose Matrix:
10 50 90 45
20 60 15 55
30 70 25 65
40 80 35 75

Final Matrix After Diagonal Swapping:
45 50 90 10
20 15 60 55
30 25 70 65
75 80 35 40


Conditions
Use Python nested lists.
Matrix size must be taken from the user.
Do not use NumPy.
Do not use zip().
Do not use built-in matrix operations.
Do not modify the original matrix.

'''
n=int(input("Enter row size: "))
m=int(input("Enter column size: "))
matrix=[]
for i in range(n):
    r=[]
    for j in range(m):
        a=int(input("enter {} element of row {}: ".format(j+1,i+1)))
        r.append(a)
    matrix.append(r)

print("\nOriginal matrix:")
for i in matrix:
   print(*i)

print("\nDiagonal Element: ")
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i==j:
           print(matrix[i][j],end=" ")

print("\nSecondary Diagonal element: ")
for i in range(n):
    print(matrix[i][n-1-i],end=" ")


print("\nTranspose of matrix:")
t=[]
for i in range(m):
    r=[]
    for j in range(n):
       r.append(matrix[j][i])
    t.append(r)

for i in t:
   print(*i)

result=[]
for i in range(n):
    temp=t[i][i]
    t[i][i]=t[i][n-1-i]
    t[i][n-1-i]=temp
print("Final matrix after swapping:")

for i in t:
     print(*i)
























