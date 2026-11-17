'''6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong

---
'''
'''
n=int(input("Enter Number: "))
x=n
sum=0
y = len(str(n))
for i in range(1,y+1):
	rem=n%10
	sum=sum+(rem**y)
	n=n//10
print(sum)
if sum==x:
	print("{} is Armstrong Number".format(sum))
else:
	print("{} is not Armstrong Number".format(sum))
'''
n=int(input("Enter Number: "))
x=n
sum=0
y = len(str(n))


while n>0:
	rem=n%10
	sum=sum+(rem)**y
	n=n//10
print(sum)
if x==sum:
	print("{} is Armstrong Number".format(sum))
else:
	print("{} is not  Armstrong Number".format(sum))
	
