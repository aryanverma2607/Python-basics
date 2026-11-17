'''
*9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''
n=int(input("Enter Number: "))
x=len(str(n))
count=0
for i in range(x):
	rem=n%10
	if rem%2==0:
		count+=1
	n//=10

while n>0:
	rem=n%10
	if rem%2==0:
		count+=1
	n//=10
if x==count:
	print("All Even")
else:
	print("Not All Even")