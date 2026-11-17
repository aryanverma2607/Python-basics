'''
3.
# Assignment: Prime Number Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them


## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---
---
'''
import math
size=int(input("Enter size of list: "))
new=""
l1=[]
cp=0
cn=0
for i in range(size):
	x=int(input("Enter element of list : "))
	l1.append(x)
print(l1)
largest=l1[0]
prime=[]
for i in l1:
	for j in (2,int(math.sqrt(i))):
		if i%j==0:
			break
	else:
		new=new+str(i) + " "
		prime.append(i)
if prime==[] or new=="":
	a=prime
	b=0
else:
	a=max(prime)
	b=new

print('''
''')
print("Prime number:",b)
print("Prime count:",len(prime))
print("Non Prime count:",len(l1)-len(prime))
print("Largest prime number:",a)
print("Prime list:",a)
print("Sorted prime List:",sorted(prime))
