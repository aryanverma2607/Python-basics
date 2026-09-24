'''Assignment 5: Shopping Bill Calculator
A retail shop wants to calculate the total bill for a customer.
Create a class ShoppingBill with the following attributes:
Product name
Product price
Quantity
Discount percentage
GST percentage

Create the following methods:
calculate_subtotal() – Calculate price × quantity.
calculate_discount() – Calculate the discount amount.
calculate_gst() – Calculate GST on the discounted amount.
calculate_final_bill() – Calculate the final payable amount.
display_bill() – Display the complete bill details.

Formula:
Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST
'''

class shoppingbill:
    def values(self):
        self.pname=input("Enter product name:")
        self.price=int(input("Enter product price:"))
        self.quantity=int(input("Enter product quantity:"))
        self.discount=int(input("Enter discount percentage:"))
        self.gst=int(input("Enter GST percentage:"))
    def calculate_subtotal(self):
        self.subtotal=self.price*self.quantity
    def calculate_discount(self):
        self.discounted=self.subtotal-(self.subtotal*(self.discount/100))
    def calculate_gst(self):
        self.gst1=self.discounted*self.gst/100
    def final_bill(self):
        self.bill=self.discounted + self.gst1
    def display(self):
        print(f"""\nProduct name: {self.pname}
Product price : {self.price}
Product quantity : {self.quantity}
Discount : {self.discount}
GST : {self.gst}
Total : {self.subtotal}
Total (discount) : {self.discounted}
Total after (GST) : {self.gst1}
Final Bill : {self.bill}""")

s=shoppingbill()
s.values()
s.calculate_subtotal()
s.calculate_discount()
s.calculate_gst()
s.final_bill()
s.display()
'''
class bill :
    def entry(self,name,price,quantity,dis_percentage,gst_per):
        self.name= name
        self.price=price
        self.quantity=quantity
        self.dis_percentage=dis_percentage
        self.gst_per =gst_per

    def calculate_subtotal(self):
        self.subtotal= self.price * self.quantity

    def calculate_discount(self):
        self.discount=self.subtotal - self.dis_percentage
        self.discounted=self.subtotal-(self.subtotal*(self.discount/100))

    def gst(self):
        self.g= self.discount*self.gst_per /100

    def final_bill(self):
        self.bill=self.discount +self.g

    def display(self):
        print('subtotal =',self.subtotal,'Discount =',self.discount,'Gst added =',self.g ,'Final bill =',self.bill)

b1=bill()
name=input('enter customer name :')
price=int(input('enter price :'))
quantity=int(input('enter quantity of product :'))
dis_percentage=int(input('enter discount percentage :'))
gst_per=int(input('enter gst percentage :'))

b1.entry(name,price,quantity,dis_percentage,gst_per)
b1.calculate_subtotal()
b1.calculate_discount()
b1.gst()
b1.final_bill()
b1.display()
'''