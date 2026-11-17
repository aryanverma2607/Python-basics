'''
3. Multiplication Table
A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
Write a program to print the *multiplication table of a given number up to 10 using loops*.

Input: n = 6
Output:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60

---
'''
n=int(input("Enter Number: "))

i=1
while i<=10:
	print(f"{n} x {i} = {n*i}")
	i=i+1

for i in range(1,11):
	print(f"{n} x {i} = {n*i}")