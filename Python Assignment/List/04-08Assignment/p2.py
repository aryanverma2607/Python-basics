'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []

'''
size=int(input("Enter size of list: "))
l1=[]
sum=0
for i in range(size):
	x=int(input("Enter element of list : "))
	l1.append(x)
print(l1)
for i in range(0,size):
	sum=sum+l1[i]
average=sum//size
print("Average = ",average)
for i in l1:
	if average<i:
		new=i
print("Above Average = ",new)
for i in l1[:]:          #copy of list 
	if i<15000:
		l1.remove(i)
print(l1)

