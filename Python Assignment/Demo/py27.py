'''1.
Mirror Difference Transaction Verification System(3.5 marks)
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified

'''
import math
num=int(input("Enter number = "))
temp=num
rev=0
i=0
while num>0:
	r=num%10
	rev=rev*10+r	
	num=num//10
print("Reverse = {}".format(rev),end=" ")
diff = abs(rev-temp)
count=len(str(diff))
print("Difference = {}".format(diff),end="")
print("Digit = {}".format(count),end="")
if diff==0:
	print("Perfect Match")
elif diff%9==0:
	print("Verified")
else:
	print("Rejected")