'''Assignment 9: Product Inventory Management
A shopkeeper wants to manage the stock of a product.
Create a class Product with the following attributes:

Product ID
Product name
Price
Available quantity

Create the following methods.
add_stock() – Increase the available quantity.
sell_product() – Decrease the available quantity.
calculate_stock_value() – Calculate price × available quantity.
display_product() – Display product and stock details.

Sample operations:
Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3

Expected result:
Available Quantity: 12
Total Stock Value: 540000

'''
class product:
    def Pro_details(self):
        self.id=int(input("Enter Product ID:"))
        self.name=input("Enter Product Name:")
        self.price=int(input("Enter Product Price:"))
        self.quantity=int(input("Enter Available Quantity:"))
    def add_stock(self):
        self.add=int(input("Enter Stock to add:"))
        self.quantity=self.quantity + self.add
    def sell_stock(self):
        self.sell=int(input("Enter Stock to Sell:"))
        self.quantity=self.quantity-self.sell
    def stock_value(self):
        self.sprice=self.price*self.quantity
    def display(self):
        print(f"""Available Quantity: {self.quantity}
Total Stock Value: {self.sprice}""")

p=product()
p.Pro_details()
p.add_stock()
p.sell_stock()
p.stock_value()
p.display()