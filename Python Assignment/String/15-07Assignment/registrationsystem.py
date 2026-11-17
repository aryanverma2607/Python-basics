'''
6. Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppercase letters, lowercase
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
alphabets and digits - Convert all alphabets to lowercase - Remove
duplicate alphabets - Arrange alphabets in ascending order - Arrange
digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”

Test Case 1 Input: Enter registration code: zBc@638

Output: Result: bcz863

Test Case 2 Input: Enter registration code: 5Br$dE654b

Output: Result: bder6554

Test Case 3 Input: Enter registration code: A9@C3d#6B1a

Output: Result: abcd9631

Test Case 4 Input: Enter registration code: X#X@M2A4x7

Output: Result: amx742

Test Case 5 Input: Enter registration code: r@T#y

Output: Result: rty No Digits Found

===================================================
'''

a=input("Enter Registration code = ").lower()
alpha=""
digit=""
r=""
i=0
while i<len(a):
	if a[i]>="a" and a[i]<="z":
		alpha=alpha+a[i]
		i=i+1
	elif a[i]>="0" and a[i]<="9":
		digit=digit+a[i]
		i=i+1
	else:
		i=i+1
		continue
alpha=("".join(sorted(alpha)))
digit=("".join(sorted(digit)))
#print(alpha)
digit=digit[::-1]
#print(digit)
newalpha=""
newdigit=""
for i in range(len(alpha)):
	if i+1<len(alpha):
		if alpha[i]==alpha[i+1]:
			continue
		else:
			newalpha=newalpha+alpha[i]

if newalpha!="":
	newalpha=newalpha+alpha[-1]
else:
	newalpha=""
if newalpha=="":
	c=newalpha+digit
	print(f"Result : {c}")
	print("No character found ")
elif digit=="":
	c=newalpha+digit
	print(f"Result : {c}")
	print("No Digit found ")
else:
	c=newalpha+digit
	print(f"Result : {c}")


'''
if digit!="":
	newdigit=newdigit+digit[-1]
else:
	newdigit=""
'''
'''
for i in range(len(digit)):
	if i+1<len(digit):
		if digit[i]==digit[i+1]:
			continue
		else:
			newdigit=newdigit+digit[i]
'''