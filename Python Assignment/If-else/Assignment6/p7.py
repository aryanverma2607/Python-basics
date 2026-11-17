'''A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹1000
'''
balance=int(input("Enter Balance: "))
if balance<=1000:
	print("Withdrawal Not Allowed")
elif balance<=5000:
	print("Maximum WIthdrawal limit : ₹1000")
else:
	print("Maximum WIthdrawal limit : ₹5000")
