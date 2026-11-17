'''
5.
Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145
'''
x=int(input("Enter Number = "))
y=int(input("Enter Number = "))
for i in range(x,y+1):	
	temp=i
	fact=1
	i=1
	sum=0
	while x>=i:
		fact=fact*i
		sum=sum+fact
		i=i+1
	else:
		if sum==temp:
			print(i,end=" ")

'''
	if i<1:
		print("NOt Strong number")
	else:
		temp=i
		fact=1
		c=1
		sum=0
		while i>0:
			r=temp%10
			j=1
			while r>=j:
				fact=fact*j
				j=j+1
			y=fact
			fact=c
			c=fact
			temp=temp//10
			sum=sum+y
		if sum==x:
			print(F"{x} is a Strong Number")
'''
	

		