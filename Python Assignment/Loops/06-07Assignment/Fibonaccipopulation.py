'''
3.

Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2
'''
n=int(input("Enter number = "))
a=0
b=1
sum=1
count=0
print("Population Growth :",end=" ")
print(a,b,end=" ")
for i in range(0,(n+1)-3):
	s=a+b
	sum=sum+s
	print(s,end=" ")
	if s>5:
		count=count+1
	a=b
	b=s
print()
print("Total Population = ",sum)
print("Months with Population = ",count)