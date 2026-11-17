'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''
id=input("Enter Employee ID = ")
i=0
count=0
count1=0
count2=0
if len(id) != 8:
	print(f"InValid Employee Id = {id}")
else:
	if id[0]=="E" and id[1]=="M" and id[2]=="P":
			count=count+1
	while i<len(id):
		if id[i]>="0" and id[i]<="9":
			count1=count1+1
		else:
			count2=count2
		i=i+1
	if count==1 and count1==5:
		print(f"Valid Employee Id = {id}")
	else:
		print(f"InValid Employee Id = {id}")