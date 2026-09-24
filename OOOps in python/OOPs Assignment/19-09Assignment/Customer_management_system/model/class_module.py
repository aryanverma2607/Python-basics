'''============================================================
ASSIGNMENT 6 – CUSTOMER MANAGEMENT SYSTEM
=========================================

Create a Customer class inside:

models/customer.py

ATTRIBUTES:

* customer_id
* customer_name
* city
* purchase_amount

TASKS:

1. Take details of 5 customers.
2. Create Customer objects.
3. Store all objects in a list.
4. Display all customers.
5. Display customers from a particular city.
6. Display customers whose purchase amount is greater than 10,000.
7. Find the customer having the highest purchase amount.
8. Calculate total sales.
9. Calculate average purchase amount.
10. Search customer using Customer Id.

SAMPLE DATA:

101 Amit Indore 12000
102 Rahul Bhopal 8000
103 Priya Indore 15000
104 Neha Pune 22000
105 Rohit Indore 7000

EXPECTED OUTPUT:

Customers from Indore:

101 Amit 12000
103 Priya 15000
105 Rohit 7000

Customers with purchase amount greater than 10000:

101 Amit 12000
103 Priya 15000
104 Neha 22000

Highest Purchase Customer:

104 Neha 22000

Total Sales:

64000

Average Purchase Amount:

12800

Search Customer Id: 103

Customer Found:

103 Priya Indore 15000
'''
customers=[]
class customer:
    def __init__(self):
        self.c_id=int(input("Enter Customer ID:"))
        self.c_name=input("Enter Customer Name:")
        self.city=input("Enter Customer City:")
        self.amount=int(input("Enter Amount:"))
        customers.append(self)

    def display(self):
        print("\nCustomer Details:")
        for i in customers:
            print(i.c_id,i.c_name,i.city,i.amount)

    def customer_city(self):
        self.city=input("\nEnter City:")
        for i in customers:
            if i.city==self.city:
                print(i.c_id,i.c_name,i.city,i.amount)

    def greater_10k(self):
        print("\nCustomers with purchase amount greater than 10000:")
        for i in customers:
            if i.amount>10000:
                print(i.c_id,i.c_name,i.city,i.amount)

    def highest(self):
        print("\nHighest Purchase Customer:")
        high=0
        for i in customers:
            if i.amount>high:
                high=i.amount
        for i in customers:
            if i.amount==high:
                print(i.c_id,i.c_name,i.city,i.amount)

    def total(self):
        total=0
        print("\nTotal Amount:")
        for i in customers:
            total=total + i.amount
        print(total)

    def average(self):
        total=0
        print("\nAverage Amount:")
        for i in customers:
            total=total + i.amount
        print(total/len(customers))

    def found(self):
        self.id=int(input("\nEnter Customer ID:"))
        for i in customers:
            if i.c_id==self.id:
                print(i.c_id,i.c_name,i.city,i.amount)
                break
        else:
            print("Customer not found")

    