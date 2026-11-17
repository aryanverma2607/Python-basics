'''6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000
'''
salary=int(input("Enter Salary: "))
a=int(input("Enter Years of Experience: "))

if a>10:
	bonus=salary*(20/100)
elif a>=5 and a<10:
	bonus=salary*(10/100)
elif a>=2 and a<5:
	bonus=salary*(5/100)
else:
	bonus=0
print(f"Bonus Amount:₹{int(bonus)}")
