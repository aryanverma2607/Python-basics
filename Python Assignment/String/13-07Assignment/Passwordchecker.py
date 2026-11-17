'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''
password=input("Enter Password : ")
upper=0
lower=0
space=0
number=0
digit=0
special=0
i=0
if password[0]>="A" and password[0]<="Z":
	upper=1
if password[len(password)-1]>="0" and password[len(password)-1]<="9":
	digit=1
while i<len(password):
	ch=password[i]
	if ch>="A" and ch<="Z":
		upper=1
	elif ch>="a" and ch<="z":
		lower=0
	elif ch==" ":
		space=1
	elif ch>="0" and ch<="9":
		number=2
	else:
		special=1
	i=i+1
if upper==1 and digit==1 and number==2 and space==0 and special==1 and len(password)>=8 and len(password)<=15:
	print("Secure Password")
else:
	print("INSecure Password")


