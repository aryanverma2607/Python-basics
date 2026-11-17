'''4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050
'''
amount=int(input("Enter Purchase amount: "))
if amount>=5000:
	discount=amount*0.2
elif amount>=2000 and amount<=5000:
	discount=amount*0.1
else:
	discount=amount*0.05
print("Final amount :",int(amount-discount))