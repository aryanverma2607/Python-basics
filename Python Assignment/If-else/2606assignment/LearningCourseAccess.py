'''1. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
'''
S_type=input("Subscription Type = ").lower()
C_progress=int(input("Course Progress = "))
T_score=int(input("Test Score = "))

if S_type=="premium":
	if C_progress>=80:
		if T_score>=70:
			print("Access Status = Certificate")
		else:
			print("Access Status = Retry Test")
	elif C_progress<80:
		print("Access Status = Complete Course")
elif S_type=="basic":
	if C_progress>=50:
		print("Access Status = Limited access")
	else:
		print("Access Status = Lock Content")
else:
	print("Access Status = Denied Access")