'''4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program
'''

age=int(input("Enter Age:"))
bmi=int(input("Enter Body Mass Index:"))
if age>=18:
	print("Allowed For Gym")
	if bmi>26:
		print("Enroll if weight loss program")
else:
	pass