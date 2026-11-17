'''
4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount
 	* First 100 units → ₹5 per unit
 	* Next 100 units → ₹7 per unit
 	* Above 200 units → ₹10 per unit
3 → Apply Surcharge
	* If bill > 2000 → 10% surcharge
	* Otherwise → 5% surcharge
4 → Display Final Bill 
5 → Exit
'''
while True:
	print("1. Enter Units Consumed")
	print("2. Calculate Bill Amount")
	print("3. Apply Surcharge")
	print("4. Final Bill")
	print("5. Exit")
	n=int(input("Enter Option = "))
	match n:
		case 1:
			unit=input("Enter Units consumed = ")
			if unit=="":
				print("Please enter units consumed first")
			else:
				print("Units Recorded Successfully")
				units=int(unit)
		case 2:
			if unit=="":
				print("Please enter units consumed first")
			else:
				if units<=100:
					bill=units*5
					print(bill)
				elif units<=200:
					bill=100*5+(200-units)*7
					print(bill)
				else:
					bill=100*5+100*7+(units-200)*10
					print(bill)
		case 3:
			if unit=="":
				print("Please enter units consumed first")
			else:
				if bill>2000:
					bill1=bill*0.1
					final_bill=int(bill+bill1)
				else:
					bill2=bill*0.05
					final_bill=int(bill+bill2)
		case 4:
			if unit=="":
				print("Please enter units consumed first")
			else:
				print("Final Bill = ",final_bill)
		case 5:
			print("Exiting program...THANK YOU!")
			break
		case __:
			print("DHANG SE NUMBER DAL")
			