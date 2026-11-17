'''
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012
'''
a=input("Enter Account number = ")
print("*"*(len(a)-4),end="")
for i in range(len(a)-4,len(a)):
	print(a[i],end="")


