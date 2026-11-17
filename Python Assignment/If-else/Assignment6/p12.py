'''12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
'''

bill=int(input("Enter Bill Amount: "))
if bill<=1000:
	tax=bill*0.05
elif bill<5000:
	tax=bill*0.12
else:
	tax=bill*0.18
if bill>=3000:
	tax=int(tax+200)
print("Final Bill Amount: ₹{}".format(bill+tax))