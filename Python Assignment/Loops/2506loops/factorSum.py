'''
6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12
'''
a=int(input("Enter number : "))
sum=0
i=1
while a>=i:
	if a%i==0:
		sum=sum+i
	i=i+1
print("Sum = ",sum)


'''
for i in range(1,a+1):
	if a%i==0:
		sum=sum+i
	i=i+1
print("Sum = ",sum)
'''
