'''
3.

 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit
'''
while True:
	print("1. Deposit Money")
	print("2. Withdraw Money")
	print("3. Check Balance")
	print("4. Apply Interest")
	n=int(input("Enter Option = "))
	match n:
		case 1:
			amount=input("Enter Amount = ")
			if amount=="":
				print("No balance available. Please deposit first")
			else:
				print("Amount deposited Successfully")
				Amount=int(amount)
		case 2:
			if amount=="":
				print("No balance available. Please deposit first")
			else:
				withdraw=int(input("Enter Withdraw amount = "))
				if withdraw>Amount:
					print("Insufficient Balance")
				else:
					print("Withdrawal Successful")
		case 3:
			if amount=="":
				print("No balance available. Please deposit first")
			else:
				balance=Amount-withdraw
				print("Available balance =",balance)
		case 4:
			if amount=="":
				print("No balance available. Please deposit first")
			else:
				interest=500
				print("Updated Balance = ",balance+interest)
		case 5:
			print("Exiting Program...THANK YOU!")
			break
		case __:
			print("Invalid Choice.Please try Again")
