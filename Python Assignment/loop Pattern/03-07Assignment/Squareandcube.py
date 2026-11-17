#WAP to print Square,Cube and Square root of all numbers from 1 to n
import math
n=int(input("Enter Number = "))
print("Squares Upto {}".format(n))
for i in range(1,n+1):
	sq=i*i
	print(sq,end=" ")
print()
print("Cubes Upto {}".format(n))
for i in range(1,n+1):
	cube=i**3
	print(cube,end=" ")
print()
print("Square Root Upto {}".format(n))
for i in range(1,n+1):
	sqrt=math.sqrt(i)
	r=round(sqrt,3)  #this will round the values to 3 decimals
	print(r,end=" ")
