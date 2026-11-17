'''1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID
'''
age=int(input("Enter your Age "))
id=input("Do you have valid ID(YES/NO)").lower()
if age>=18:
	if id=="yes":
		print("Eligible to vote")
		print("Allowed Inside Booth")
else:
	print("Under Age ")