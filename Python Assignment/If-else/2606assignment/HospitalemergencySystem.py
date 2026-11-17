'''
2. Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU
'''
A=int(input("Age = "))
S=input("Severity = ").lower()
I=input("Insurance = ").lower()
if S=="critical":
	if A>=60:
		print("Treatment = Immediate ICU")
	else:
		print("Treatment = Emergancy Ward")
if S=="moderate":
	if I=="yes":
		print("Treatment = Priority Treatment")
	else:
		print("Treatment = Genral Queue")
if S=="low":
	if A<=10:
		print("Treatment = Pediatric Priority")
	else:
		print("Treatment = Wait")