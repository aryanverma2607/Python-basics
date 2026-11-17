'''
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12
'''
phone=input("Enter number = ")
count=0
for i in phone:
	if i>="0" and i<="9":
		count=count+1
	else:
		count=count
print(f"Total Digits :{count}")