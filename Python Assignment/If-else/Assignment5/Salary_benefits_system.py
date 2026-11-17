'''7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus
'''

salary=int(input("Enter Salary:"))
if salary >= 30000:
	print("Eligible For PF")
if salary >= 50000:
	print("Eligible for bonus")