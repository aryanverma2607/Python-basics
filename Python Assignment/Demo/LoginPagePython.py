mail1=""
password1=""
while True
	login=input("Do you have account(Y/N) = ").lower()
	if login=="y" or login=="yes":
		mail=input("Enter mail = ")
		password=input("Enter Password = ")
		if mail==mail1 and password=password1:
			print("Login Successfully")
	else:
		print("Register here")
		name=input("Enter Your Name = ")
		mail1=input("Enter Your mail Id = ")
		while True:
			password1=input("Enter Password = ")
			if len(str(password)) >=8:
				print("Strong Password")
			else:
				print("Weak Password")
			phone=int("Enter your phone number ")
			if len(str((phone))==10:
				break
			else:
				print("Invalid Phone Number")
				print("Enter Again")
		print("Register Successfully")
	