'''
11.

=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
'''
n=int(input("Enter number of product: "))
product=[]
for i in range(n):
	name=input("Enter product name: ")
	product.append(name)
p={}
for i in product:
	p[i]=p.get(i,0)+1
for k,v in sorted(p.items()):
	print(k,":",v)