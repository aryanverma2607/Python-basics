'''
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 4

---
'''
print("""4. Longest Consecutive Sequence
===============================""")



n=int(input("Enter size of List:"))
l=[]
for i in range(n):
	l.append(int(input("Enter Element:- ")))
print()
vis=[]
count1=0
for i in l:
	count=1
	while i+1 in l:
		count+=1
		i+=1
	if count>count1:
		count1=count

print("Longest Consectuive Sequence : ",count1)