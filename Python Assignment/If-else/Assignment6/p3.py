'''3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000
'''
income=int(input("Enter Annual income: "))
if income<=250000:
	tax=0
elif income<=500000:
	income-=250000
	tax=income*0.05
elif income>500000 and income<=1000000:
	income-=250000
	tax=income*0.2
else:
	income-=250000
	tax=income*0.3
print(F"Tax Payable ₹{tax}")