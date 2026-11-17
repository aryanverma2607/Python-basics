'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''

category=input("Enter Course Category(Programming/Design/Marketing): ").lower()
user_type=input("Enter User Type: ").lower()

if category=="programming":
	if user_type=="student":
		fees=5000-(5000*0.2)
	elif user_type=="workingprofessional":
		fees=5000-(5000*0.1)
	else:
		fees=5000
elif category=="design":
	if user_type=="student":
		fees=4000-4000*0.2
	elif user_type=="workingprofessional":
		fees=4000-4000*0.1
	else:
		fees=4000
elif category=="marketing":
	if user_type=="student":
		fees=3000-3000*0.2
	elif user_type=="workingprofessional":
		fees=3000-3000*0.1
	else:
		fees=3000

print("Final Course Fee:",fees)


