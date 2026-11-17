'''
====================================================================

1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found

---

'''
print("""1. First Non-Repeating Number
   ====================================================================
""")
n=int(input("Enter size of List:"))
l=[]
for i in range(n):
	l.append(int(input("Enter Element:- ")))
print()
vis=[]
for i in l:
	if i not in vis:
		count=0
		for j in l:
			if i==j:
				count=count+1
	vis.append(i)
	if count==1:
		print(i)
		break
else:
	print("No repeating character found")
