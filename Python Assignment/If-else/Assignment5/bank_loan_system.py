'''1. A bank wants to automate its loan approval process. The system should take salary,
credit score, and number of existing loans as input. If the salary is greater than or equal to 30000,
then it should check the credit score. If the credit score is greater than or equal to 750,
 the loan should be approved. Otherwise, it should check the number of existing loans.
If the existing loans are less than 2, the loan should be conditionally approved; otherwise, it should be rejected.
If the salary is less than 30000, the loan should be rejected. Display the final loan status.

Input:
salary = 40000
credit_score = 720
existing_loans = 1

Output:
Loan Status = Conditional Approval'''




salary=float(input("Enter Salary="))
creditScore=int(input("Credit Score="))
existing_loan=int(input("Existing loans="))
if salary>=30000:
	if creditScore>=750:
		print("Loan Status = Loan Should be approved")
	else:
		if existing_loan<2:
			print("Loan Status = Conditionally Approved")
		else:
			print("Loan Status = Rejected")
else:
	print("Loan Status = Rejected!!!")



