'''
7.Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:print("Not Prime")

- Find sum of alternate digits

- Check whether sum is Prime or Not

Input:
12345
Output:
Alternate Sum = 9

Not Prime
'''
num=int(input("Enter number = "))
add=0
l=len(str(num))
for i in range(1,l+1):
	r=num%10
	add=add+r
	num=num//100
print(add)
if add<0:
	print("Not Prime")
else:
	i=2
	flag=0
	while add>i:
		if add%i==0:
			flag=flag+1
			break
		i=i+1
	if flag==0:
		print("Prime")
	else:
		print("Not Prime")
