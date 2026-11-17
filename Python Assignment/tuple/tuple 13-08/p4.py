'''
=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3

'''
from collections import namedtuple
print("""=====================================================================
QUESTION 3: ONLINE SHOPPING ORDERS
====================================""")


order=namedtuple("orderdetail",["order_id","customer_name","product_name","amount"])
n=int(input("Enter number of order : "))
l1=[]
for i in range(n):
	print(f"Enter order {i+1} detail")
	id=int(input("Enter Order ID = "))
	cname=input("Enter Customer name = ")
	pname=input("Enter Product name = ")
	amount=int(input("Enter Amount = "))	
	p=order(id,cname,pname,amount)
	l1.append(p)
print(l1)
for i in l1:
	print(i.order_id,i.customer_name,i.product_name,i.amount)
print()
sum=0
highest=p.amount
for i in l1:
	if i.amount>highest:
		highest=i.amount
	sum=sum+i.amount
print(highest)
for i in l1:
	if i.amount==highest:
		print(f"""Highest Value Order:
{i.order_id} {i.customer_name} {i.product_name} {i.amount}""")
print()
print("""Total Sales:
{}""".format(sum))
print()
count=0
for i in l1:
	if i.amount>10000:
		count+=1
print("""Orders Above ₹10,000:
{}""".format(count))