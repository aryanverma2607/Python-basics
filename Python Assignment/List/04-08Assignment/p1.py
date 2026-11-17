'''
=====================================================================
1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
'''
size=int(input("Enter size of list: "))
l1=[]
count=0
for i in range(size):
	x=int(input("Enter element of list : "))
	l1.append(x)
print(l1,end="→ ")
highest=l1[0]
lowest=l1[0]
for i in l1:
	if i>75:
		count=count+1
	if highest<i:
		highest=i
	if lowest>i:
		lowest=i
print("Highest = ",highest,end=" ")
print("Lowest = ",lowest,end=" ")
print("Count Above 75 = ",count)