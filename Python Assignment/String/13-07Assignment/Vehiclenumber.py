'''
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''





v=input("Enter number = ")
a=v[:2]
b=v[2:4]
count=0
count1=0	
if v[4]==" ":
	count1=1
else:
	count1=count1

for i in v:
	if "A"<=a<="Z" or "a"<=a<="z":
		count=count+1
		if "9">=b>="0":
			count=0
		elif i==" ":
			count1=1
		else:
			count=count
	else:
		count=1
if len(v)-count1==10 and count==4:
	print("Valid Vehicle Number")
else:
	print("InValid Vehicle Number")

