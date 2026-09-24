'''
Question 3: Online Shopping System
Scenario
An e-commerce company wants to calculate the final amount payable by customers after applying discounts.
Requirements

Create a class named Product with:
product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.
Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0
'''
class product:
    def __init__(self,p_id,p_name,quantity,price):
        self.p_id=p_id
        self.p_name=p_name
        self.quantity=quantity
        self.price=price
    def total(self):
        self.total=self.quantity * self.price
    def discount(self):
        if self.total> 5000:
            self.discount=self.total*0.1
        else:
            self.discount=self.total*0.05
    def final(self):
        self.final=self.total - self.discount
    def display(self):
        print(f"""\n------ Shopping Bill ------
Product ID        : {self.p_id}
Product Name      : {self.p_name}
Quantity          : {self.quantity}
Price Per Item    : {self.price}
Total Amount      : ₹{self.total}
Discount          : ₹{self.discount}
Final Amount      : ₹{self.final}""")

p=product("P101","Laptop",2,35000)
p.total()
p.discount()
p.final()
p.display()