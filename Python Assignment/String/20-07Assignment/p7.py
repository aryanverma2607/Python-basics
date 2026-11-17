'''
# 7. Enterprise Password Pattern Strength Analyzer
A cybersecurity company wants to validate advanced passwords.
## Conditions:
* Minimum 10 characters
* At least:
  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:
text
Pyth@n1234
### Output:
text
Strong Password

### Input:
text
Paaass@12
### Output:
text
Weak Password
'''
string=input("Input :")
upper=0
lower=0
digit=0
special=0
space=0
if len(string)>=10:
	for i in range(len(string)):
		if "a"<=string[i]<="z":
			lower=1
		elif "A"<=string[i]<="Z":
			upper=1
		if "0"<=string[i]<="9":
			digit=1
		if string[i]==" ":
			space=1
		else:
			special=1
		count=0 	
		for i in range(len(string)):
			if i+1<len(string):
				if string[i]== string[i+1]:
					count=count+1
				else:
					continue	
	if upper==1 and lower==1 and digit==1 and special==1 and space==0 and count==0:
		print("Strong Password")
	else:
		print("Weak Password")
else:
	print("Weak Password")