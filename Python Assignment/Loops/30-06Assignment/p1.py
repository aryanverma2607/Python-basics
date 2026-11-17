'''
1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime
'''
import math
n=int(input("Number = "))
a=n
sum=0
rev=0
while n>0:
	r=n%10
	sum=sum+r
	rev=rev*10+r
	n=n//10
sub=abs(a-rev)
print("Sum of Digit = ",sum)
print("Reverse = ",rev)
print("Difference = ",sub)
sum1=sum+sub
print("Final Result = ",sum1)
i=2
count=0
while sum>i:
	if sum%i==0:
		count=count+1
		break
	i=i+1
if count==0:
	print("Print Number")
else:
	print("Not Prime Number")