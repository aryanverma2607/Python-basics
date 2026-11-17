'''
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3
'''
n=int(input("Number:"))
count=0
while n>0:
	r=n%10
	if r%2==0:
		pass
	else:
		count=count+1
	n=n//10
print("Odd Digits Count = ",count)


'''
for i in range(len(str(n))):
	d=n%10
	if d%2==0:
		pass
	else:
		count=count+1
	n=n//10		

print("Odd Digits Count = ",count)
'''

