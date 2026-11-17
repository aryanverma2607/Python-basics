'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''
a=input("Enter first product code: ")
b=input("Enter second product code: ")
string1=""
string2=""
x=1
for i in a:
	if i==" ":
		continue
	else:
		string1=string1+i
for i in b:
	if i==" ":
		continue
	else:
		string2=string2+i
a=" ".join(sorted(string1))
b=" ".join(sorted(string2))
if a==b:
	print("BOTH PRODUCT CODES ARE MATCHING")
else:
	print("BOTH PRODUCT CODES ARE NOT MATCHING")

			
