'''10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate
'''
marks,attendence=map(int,input("Enter your marks and Attendence separated by comma:").split(","))
if marks>=40:
	print("Pass")
	if attendence>=75:
		print("Eligible For Certificate")
