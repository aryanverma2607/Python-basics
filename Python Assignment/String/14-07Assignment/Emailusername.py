'''
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''

username=input("Enter Username = ")
letter=0
space=0
if len(username)<=5 or len(username)>=12:
	print("Invalid Username")
else:
	if username[0]>="A" and username[0]<="Z" or username[0]>="a" and username[0]<="z":
		letter=letter
	for s in username:
		if s>="A" and s<="Z" or s>="a" and s<="z" or s>="0" and s<="9" or s=="_":
			letter=letter
		else:	
			letter=letter+1
			break
	if letter==0 and 5<=len(username)<=12:
		print("Valid Username")
	else:
		print("InValid Username")

