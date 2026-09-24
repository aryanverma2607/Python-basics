'''Assignment 7: Mobile Phone Data Usage
A mobile user wants to calculate their remaining internet data.

Create a class MobilePlan with the following attributes:
Customer name
Mobile number
Total data in GB
Used data in GB
Validity in days

Create the following methods:
calculate_remaining_data() – Calculate remaining data.
calculate_usage_percentage() – Calculate the percentage of data used.
display_plan() – Display the plan details and results.

Sample data:

Total Data: 50 GB
Used Data: 18 GB
Validity: 28 days

Expected result:

Remaining Data: 32 GB
Usage Percentage: 36.0%
'''
class mobile_data:
    def customer(self):
        self.cname=input("Enter Customer Name:")
        self.mobile_no=int(input("Enter Mobile Number:"))
        self.data=int(input("Enter Total Data In GB:"))
        self.used=int(input("Enter Used Data In GB:"))
        self.validity=int(input("Enter Validity In Days:"))
    def remaining_data(self):
        self.remained=self.data-self.used
    def usage_percentage(self):
        self.remain=(self.used/self.data)*100
    def display(self):
        print(f"""Remaining Data: {self.remained} GB
Usage Percentage: {self.remain}%""")

m=mobile_data()
m.customer()
m.remaining_data()
m.usage_percentage()
m.display()