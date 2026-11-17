'''4. A gym provides personalized plans based on age, weight, and fitness goal.
The system should take age, weight, and goal (weight loss or muscle gain) as input.
 If the age is greater than or equal to 18, then check the weight. If the weight is greater than or
 equal to 80, then check the goal. If the goal is "weight loss", assign "Cardio Plan"; otherwise, assign
"Strength Plan". If the weight is less than 80, assign "General Fitness Plan". If the age is less than 18, display
 "Not Allowed". Display the recommended plan.

Input:
Age = 25
Weight = 85
Goal = weight loss

Output:
Plan = Cardio Plan
'''

age=int(input("Enter Age = "))
weight=float(input("Weight = "))
fitness_goal=input("Weight loss or Muscle Gain = ").upper()
if age>=18:
	if weight>=80:
		if fitness_goal=="WEIGHT LOSS":
			print("Plan = Cardio Plan")
		else:#case of Muscle Gain
			print("Plan = Strength Plan")
	else:
		print("Plan = General Fitness Plan")
else:
	print("Not Allowed")
