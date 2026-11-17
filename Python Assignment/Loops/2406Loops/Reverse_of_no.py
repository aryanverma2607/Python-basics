'''4. Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.

Input: 1234
Output: 4321

---
'''
n=int(input("Enter Number: "))
a=len(str(n))
rev=0
for i in range(a):
	rev=rev*10+n%10
	n=n//10
print("Reversed number is : ",rev)
while n>0:
	rev=rev*10+n%10
	n=n//10
print("Reversed number is : ",rev)