'''
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]

'''
m=int(input("Enter Size of List:"))
l=[]
for i in range(m):
	l.append(int(input("Enter element:")))
print()
product=[]
for i in range(m):
	p=1
	for j in range(m):
		if i!=j:
			p=p*l[j]
	product.append(p)
print(product)
		