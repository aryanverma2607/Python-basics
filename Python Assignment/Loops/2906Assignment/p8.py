'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''
n=int(input("Enter Number = "))
x=str(n)
largest=1
smallest=9
count=0
for i in x:
	if i=="0":
		largest=0
		smallest=0
for i in range(len(str(n))):
	r=n%10
	if r>=largest:
		largest=r
	elif r<smallest:
		smallest=r
	n=n//10
sum=largest+smallest
print("Largest Digit = ",largest)
print("Smallest digit = ",smallest)
print("Sum = ",sum)
if sum<=0:
	print("Not prime ")
else:
	for i in range(2,sum//2):
		if sum%i==0:
			count=count+1
		i=i+1
	if count==0:
		print("Prime number")
	else:		
		print("Not Prime Number")