'''
2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the *factorial of a given number using loops*.

Input: n = 5
Output: Total Ways = 120

---
'''
n=int(input("Enter Number: "))
fact=1
for i in range(n,1,-1):
	fact=fact*i
print("Total Ways: ",fact)
fact=1
i=1
while n>=i:
	fact=fact*i
	i=i+1
print("Total Ways: ",fact)