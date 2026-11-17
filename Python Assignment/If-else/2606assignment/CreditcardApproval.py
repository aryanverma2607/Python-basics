'''
1. Smart Credit Card Approval System

A bank evaluates credit card applications based on income, credit score, employment type, and existing debt.

If income is greater than or equal to 50000, then check credit score. If credit score is greater than or equal to 750, then check debt. If debt is less than 20000, approve Premium Card; otherwise approve Gold Card. If credit score is less than 750, then check employment type. If employment is government and credit score is at least 650, approve Gold Card; otherwise reject.

If income is less than 50000, then check if income is at least 30000 and credit score is at least 700. If yes, approve Silver Card; otherwise reject.

Input:
Income = 45000
Credit Score = 720
Employment = private
Debt = 10000

Output:
Card Type = Silver Card
'''
income=int(input("Income = "))
Credit_Score=int(input("Credit Score = "))
Employment_type=input("Employment(Government/Private) = ").lower()
Existing_Debt=int(input("Debt = "))
if income>=50000:
	if Credit_Score>=750:
		if Existing_Debt<20000:
			print("Card Type = Premium Card")
		else:
			print("Card Type = Gold Card")
	else:
		if Employment_type=="government":
			if Credit_Score>=650:
				print("Card Type = Gold Card")
			else:
				print("Rejected")