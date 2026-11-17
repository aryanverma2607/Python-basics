'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''
n=int(input("Enter Number = "))
temp=n
sum=0
pro=1
for i in range (len(str(n))):
	r=n%10
	sum=sum+r
	pro=pro*r
	n=n//10
if sum==pro:
	print(f"{temp} is Spy Number")
else:
	print(f"{temp} is Not A Spy Number")
