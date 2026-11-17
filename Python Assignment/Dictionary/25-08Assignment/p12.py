'''
12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza

'''
n=int(input("Enter number of food item: "))
food=[]
for i in range(n):
	a=input("Enter order name: ")
	food.append(a)
d={}
for i in food:
	d[i]=d.get(i,0)+1
print(d)
most=0
for k,v in d.items():
	if v>most:
		most=v
for k,v in d.items():
	if v==most:
		print("Most ordered : {}".format(k))