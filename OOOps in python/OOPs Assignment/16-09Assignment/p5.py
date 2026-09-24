'''Question 5: Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.
Requirements
Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.
Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0
'''
class hotel:
    def __init__(this,id,name,days,charge):
        this.id=id
        this.name=name
        this.days=days
        this.charge=charge
    def Bill(this):
        this.bill=this.days*this.charge
    def gst(this):
        this.gst=this.bill*0.12
    def final_bill(this):
        this.final_bill=this.bill+this.gst
    def display(this):
        print(f"""\n------ Hotel Bill ------
Guest ID              : {this.id}
Guest Name            : {this.name}
Number of Days        : {this.days}
Room Charge Per Day   : ₹{this.charge}
Room Bill             : ₹{this.bill}
GST (12%)             : ₹{this.gst}
Final Bill            : ₹{this.final_bill}""")

h=hotel("101","Aryan",4,2500)
h.Bill()
h.gst()
h.final_bill()
h.display()

