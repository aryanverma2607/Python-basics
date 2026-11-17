'''
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 180
Enter rating: 4

Output:
Revised Salary: ₹23600
'''
salary=int(input("Enter salary: "))
rating=int(input("Enter rating: "))

if rating==5:
	hike=salary*0.25
elif rating==4:
	hike=salary*0.2
elif rating==3:
	hike=salary*0.1
elif rating==2:
	hike=salary*0.05
else:
	hike=0
if salary<=20000:
	if rating>=4:
		new_salary=hike+2000
		print("Revised Salary: ₹",new_salary+salary)
	elif rating==3:
		print("Revised Salary: ₹",salary+hike)
	elif rating==2:
		print("Revised Salary: ₹",salary+hike)
	else:
		print("Revised Salary: ₹",salary)
else:
	print("Revised Salary: ₹",salary+hike)