'''
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
'''

web=input("Enter website: ")
count=0
if web[0]=="w" and web[1]=="w" and web[2]=="w" and web[3]==".":
	if web[len(web)-4:]==".com":
		print("Valid website")
	else:
		print("inValid website")
else:
	print("InValid website")

