'''
4.

Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

Definition

A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

An element is called a leader if:

It is greater than all elements to its right side
The element must be valid, i.e., it should not be:
Negative number
Zero

Rightmost valid element is always considered a leader.

Input Format
First line → integer n
Second line → n space-separated integers

Output Format
Single integer → sum of all valid leader elements
If no valid elements exist → return -1

Rules
Before finding leaders:

Ignore all negative values and zeros
Work only on positive numbers
Then find leaders from the filtered sequence

Test Case 1

Input:
8
16 0 17 4 -3 3 5 2

Processing:
Filtered array:
[16, 17, 4, 3, 5, 2]

Leaders:
[17, 5, 2]

Output:
24

'''
n=int(input("Enter Size:"))
l1=list(map(int,input("Enter Element:").split()))
if len(l1)!=n:
	print("List element are not properly entered")
else:
	print(l1)
	invalid=[]
	valid=[]
	for i in l1:
		if i<=0:
			invalid.append(i)
		else:
			valid.append(i)
	print("Filtered List:",valid)
	leadersum=0
	leader=[]
	for i in range(len(valid)):
		isleader=True
		for j in range(i+1,len(valid)):
			if valid[i]<=valid[j]:
				isleader=False
				break
		if isleader:
			leader.append(valid[i])
			leadersum+=valid[i]
	print("Leaders: ",leader)
	print("Leader Sum = ",sum(leader))
	print(leadersum)



