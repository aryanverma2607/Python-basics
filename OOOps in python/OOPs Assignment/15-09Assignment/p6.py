'''Assignment 6: Electricity Bill Calculator
An electricity board wants to calculate a customer's electricity bill based on units consumed.
Create a class ElectricityBill with the following attributes:
Consumer number
Consumer name
Units consumed
Rate per unit
Fixed charge

Create the following methods:
calculate_energy_charge() – Calculate units × rate per unit.
calculate_total_bill() – Add energy charge and fixed charge.
display_bill() – Display consumer details and bill amount.

Sample data:
Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600
'''
class electricitybill:
    def consumer(self):
        self.cno=int(input("Enter Consumer Number:"))
        self.cname=input("Enter Consumer Name:")
        self.unit=int(input("Enter Number Of Units Consumed:"))
        self.rate=int(input("Enter Rate Per Unit:"))
        self.fixed=int(input("Enter Fixed Charge:"))
    def calculater_energy_charge(self):
        self.charge=self.unit*self.rate
    def calculate_total_bill(self):
        self.total=self.charge+self.fixed
    def display(self):
        print(f"""\nConsumer Number: {self.cno}
Consumer Name: {self.cname}
Units Consumed: {self.unit}
Rate Per Unit: {self.rate}
Fixed Charge: {self.charge}
""")
        print(f"""\nEnergy Charge: {self.charge}
Total Bill: {self.total}""")


e=electricitybill()
e.consumer()
e.calculater_energy_charge()
e.calculate_total_bill()
e.display()