 '''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500
'''
x=int(input("Enter Starting Number = "))
y=int(input("Enter Ending number = "))
for i in range(x,y+1):
	l=len(str(i))
	temp=i
	sum=0
	for j in range(l):
		r=i%10
		sum=sum+r**l
		i=i//10
	else:
		if temp==sum:
			print(temp,end=" ")
	
	