'''

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%
'''
salary=int(input("Salary = "))
age=int(input("Age = "))
credit_s=int(input("Credit Score = "))
emi=int(input("EMI = "))
if salary>=40000:
	if age>=21 and age<=60:
		if credit_s>=750 and emi<=salary*0.4:
			print("Loan Status = Approved at 8%")
		else:
			if credit_s>=650:
				print("Loan Status = Approved at 12%")
			else:
				print("Loan Status = Rejected")
			print("Loan Status = Approved at 10%")
else:
	if salaery>=25000:
		if credit_s>=700:
			print("Loan Status = Approved at 13%")
		else:
			print("Loan Status = Rejected")