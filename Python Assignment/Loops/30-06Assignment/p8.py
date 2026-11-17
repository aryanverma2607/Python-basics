'''
8.ATM Note Counter
A bank ATM dispenses ₹100 notes.
Write a program to:
- Read withdrawal amount
- Count how many ₹100 notes needed using loop
Input:
700
Output:
Notes = 7
'''
n=int(input("Number = "))
count=0
while n>0:
	n=n-100
	count=count+1
print(count)
