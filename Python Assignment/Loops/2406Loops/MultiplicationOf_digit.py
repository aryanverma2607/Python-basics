'''
*12. Multiplication of Digits*
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.

Input: 1234
Output: 24
Even

---
'''
n=int(input("Enter Number = "))
product=1
'''for i in range(len(str(n))):
	if n%10==0:
		n=n//10
	rem=n%10
	product=product*rem
	n=n//10'''
while n>0:
	if n%10==0:
		n=n//10
	rem=n%10
	product=product*rem
	n=n//10
print("Product Of Digit : ",product)
if product%2==0:
	print("Even")
else:
	print("Odd")