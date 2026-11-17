'''
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)

'''

n=int(input("Enter number of product : "))
list=[]
for i in range(n):
	p_id=input("Enter Product ID = ")
	pname=input("Enter Product name = ")
	price=int(input("Enter Prodcut price = "))
	product=(p_id,pname,price)
	list.append(product)
print("All Product")
for i in list:
	print(i)
print()
highest=list[0][2]
lowest=list[0][2]
for i in range(n):
	if highest<list[i][2]:
		highest=list[i][2]
	if list[i][2]<lowest:
		lowest=list[i][2]
sum=0
for i in range(len(list)):
	sum=sum+list[i][2]
	if list[i][2]==highest:
		print("Costliest Product:")
		print(list[i])
	if list[i][2]==lowest:
		print("Cheapest Product:")
		print(list[i])
print()
average=sum/n
print("""Average Price:
{}""".format(average))
print()
print("Products Above ₹50,000:")
for i in range(len(list)):
	if list[i][2]>50000:
		print(list[i])


