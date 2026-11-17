'''
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found
'''
print("""8. Majority Element Detector
============================""")
print()

N=int(input("enter Size = "))
list1=[]
for i in range(N):
	list1.append(int(input("Enter Element = ")))
print(list1)
vis=[]
for i in list1:
	if i not in vis:
		count=0
		for j in list1:
			if i==j:
				count=count+1
		vis.append(i)
		if count>N/2:
			print("Majority Element = {}".format(i))
			break
else:
	print("No Majority Number Found")