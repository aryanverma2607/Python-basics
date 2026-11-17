'''
Multiplication Table Generator

Scenario:
A school learning app helps students practice multiplication tables.
The user enters a number n, and the system prints multiplication tables from 1 to n using nested loops.

Input:
Enter limit: 3
'''
n=int(input("Enter Number = "))
x=1
while x<=n:
	for i in range(1,11):
		print(x,"x",i,"=",x*i)
		i=i+1
	print()
	x=x+1