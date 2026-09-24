'''Question 2: Electricity Bill Calculator
Scenario
An electricity company wants to generate monthly bills for its customers.
Requirements

Create a class named Customer with:
customer_id
customer_name
units_consumed

Initialize the values using a constructor.
Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0
'''
class customer:
    def __init__(self,c_id,c_name,units):
        self.c_id=c_id
        self.c_name=c_name
        self.units=units
    def bill(self):
        self.cost=8
        self.fixed=150
        self.total=self.units*self.cost + self.fixed
    def display(self):
        print(f"""\n------ Electricity Bill ------
Customer ID       : {self.c_id}
Customer Name     : {self.c_name}
Units Consumed    : {self.units}
Total Bill Amount : ₹{self.total}""")

c=customer("C101","Muskan",350)
c.bill()
c.display()
