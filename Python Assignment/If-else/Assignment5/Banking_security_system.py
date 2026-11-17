'''5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password
'''
username=input("Enter Username:")
password=input("Enter password:")
passkey=len(password)
if username=="admin":
	print("Valid user")
	if passkey>=8:
		print("Strong Password")
	else:
		print("weak Password")
else:
	print("Invalid Username")