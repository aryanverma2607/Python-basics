'''
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

---
'''
print("""5. Equilibrium Index Finder
===========================""")


N=int(input("Enter size of List: "))
l1=[]
for i in range(N):
	l1.append(int(input("enter element :- ")))
print(l1)
index=0
for i in range(N+1):     #[1,2,sum=3,<-(3)->sum=3,2,1] then sum of left=sum of right then index 3 is equilibrium index
	sl=0
	sr=0
	for j in range(i-1,-1,-1):
		sl=sl+l1[j]
	for k in range(i+1,N):
		sr=sr+l1[k]
	if sl==sr:
		print("Equilibrium index = ",i)
		break
else:
	print("No equilibrium index found")


















