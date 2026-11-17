'''
5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6
'''
n=int(input("Number = "))
count=0
i=1
while n>=i:
	if n%i==0:
		count=count+1
	i=i+1
print("Count = ",count)
'''
count=0
for i in range(1,n+1):
	if n%i==0:
		count=count+1
	i=i+1
print("Count = ",count)
'''