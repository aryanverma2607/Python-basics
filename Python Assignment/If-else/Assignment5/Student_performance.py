'''2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction
'''

marks=int(input("Enter marks:"))
if marks >=40:
	print("Pass")
	if marks>=75:
		print("Distinction")
else:
	pass
	#print("Failed")