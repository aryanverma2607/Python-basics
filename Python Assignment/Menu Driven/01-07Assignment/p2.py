'''
2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first
'''
while True:
	print("1. Enter Basic Salary")
	print("2. Calculate HRA (20%) and DA (10%)")
	print("3. Calculate Net Salary")
	print("4. Tax Deduction")
	n=int(input("Enter Option = "))
	match n:
		case 1:
			x=input("Enter Number = ")
			if x=="":
				print("Please enter basic salary first")
			else:
				print("Your Salary is Recorded Successfully")
				salary=int(x)
		case 2:
			if x=="":
				print("Please enter basic salary first")
			else:
				y=int(salary*0.2)
				z=int(salary*0.1)
				print(f"HRA is {y} and DA is {z}")
		case 3:
			if x=="":
				print("Please enter basic salary first")
			else:
				y=int(salary*0.2)
				z=int(salary*0.1)
				net_salary=salary+y+z
				print(net_salary)
		case 4:
			if x=="":
				print("Please enter basic salary first")
			else:
				y=int(salary*0.2)
				z=int(salary*0.1)
				net_salary=salary+y+z
				tax=int(net_salary*0.1)
				salary1=salary-tax
				print("Salary After tax Deduction = ",salary1)
		case 5:
			if x=="":
				print("Please enter basic salary first")
			else:
				print("------Salary Slip------")
				print("Basic Salary :",salary)
				y=int(salary*0.2)
				z=int(salary*0.1)
				print("HRA:",y)
				print("DA:",z)
				net_salary=salary+y+z
				print("Net Salary:",net_salary)
				tax=net_salary*0.1
				print("Tax:",tax)
				print("Final Salary :",net_salary-tax)
		case 6:
			print("Exiting Program...Thank YOu!")
			break
		case __:
			print("Invalid Choice.Please Try Again")


















