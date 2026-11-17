'''
4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]	

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]

'''
l1=list(map(int,input("Enter element: ").split()))
pl1=[]
print(l1)
for i in l1:
	num=i
	rev=0
	while i>0:
		r=i%10
		rev=rev*10+r
		i=i//10
	if num==rev:
		pl1.append(rev)
print("palindrome:",pl1)
print("Count:",len(pl1))
print("largest:",max(pl1))	
print("Sorted:",sorted(pl1))
