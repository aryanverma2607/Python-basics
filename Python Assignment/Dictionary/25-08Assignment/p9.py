'''
9.

=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker

'''
n=int(input("Enter number of stock: "))
stock={}
for i in range(n):
	name=input("Enter stock name: ")
	stock[name]=int(input("Enter stock price:"))
for i,j in stock.items():
	if j<30:
		print(i)