'''3. Online Shopping Order History
An e-commerce company maintains order information in orders.txt.
Each order contains:
OrderID,CustomerName,Product,Quantity,Price
Task
Write a program to:
Accept order details.
Store them in the file.
Read the file.
Calculate total amount for each order.
Display the order having the highest total amount.
Formula:
Total Amount = Quantity × Price
Sample Input
Enter number of orders: 3
O101,Rahul,Laptop,1,55000
O102,Priya,Mouse,3,800
O103,Amit,Keyboard,2,1500
Expected Output
Order Details
--------------------------------
O101 Rahul Laptop   Quantity: 1 Total: 55000
O102 Priya Mouse    Quantity: 3 Total: 2400
O103 Amit Keyboard  Quantity: 2 Total: 3000
Highest Order:
Order ID: O101
Customer: Rahul
Total Amount: 55000
================
'''
n=int(input("Enter number Of Order:"))
with open("order.txt","w") as f:
    for i in range(n):
        id = input("Enter Order ID:")
        customer_name = input("Enter Customer name:")
        product_name = input("Enter Product name:")
        quantity = input("Enter product Quantity:")
        price = input('Enter Product Price:')
        f.write(id + " " + customer_name + " " + product_name + " " + quantity + " " + price + "\n")
f.close()
with open("order.txt","r") as f:
    for i in f:
        data = i.split()
        high = int(data[3])*int(data[4])
        print(high)
        total = int(quantity)*int(price)
        if total>high:
            high = total
    f.seek(0)
    for i in f:
        data = i.split()
        high = int(data[3])*int(data[4])
        total = int(quantity)*int(price)
        if total == high:
            print(f"""Highest Order:
Order ID: {data[0]}
Customer: {data[1]}
Total Amount: {int(data[3])*int(data[4])}""")
