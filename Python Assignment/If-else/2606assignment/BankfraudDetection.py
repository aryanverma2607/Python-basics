'''
2. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1
'''
a=int(input("Transaction Amount = "))
b=input("Location(International/domestic) = ").lower()
c=int(input("Account Age = "))
if a>=10000:
	#b=input("Location(International/domestic) = ").lower()
	if b=="international":
		o=input("Enter otp = ")
		if o=="ary@n":
			print("Transaction status = Allowed")
		else:
			print("Transaction Status = BLocked")
	if b=="domestic":
		if a>=50000:
			#c=int(input("Account Age = "))
			if c>=2:
				print("Transaction status = Allowed")
			else:
				print("Transaction status = Flagged")
		else:
			print("Transaction status = Allowed")
else:
	d=input("Any unusual activity (yes/no)= ").lower()
	if d=="yes":
		 print("Transaction status = Flagged")
	else:
		print("Transaction status = Allowed")