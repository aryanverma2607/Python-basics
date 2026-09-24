'''Assignment 10: Personal Expense Calculator
A person wants to calculate monthly expenses and savings
Create a class ExpenseTracker with the following attributes:
Person name
Monthly salary
Rent
Food expenses
Travel expenses
Other expenses
Create the following methods:
calculate_total_expenses() – Calculate all expenses.
calculate_savings() – Calculate salary minus total expenses.
display_expense_report() – Display salary, expenses, and savings.
Formula:
Total Expenses = Rent + Food + Travel + Other Expenses
Savings = Monthly Salary - Total Expenses
Sample data:
Monthly Salary: 60000
Rent: 12000
Food: 8000
Travel: 5000
Other Expenses: 3000
Expected result:
Total Expenses: 28000
Savings: 32000
'''
class expensetracker:
    def expense(self,name,salary,rent,food,travel,other):
        self.name=name
        self.salary=salary
        self.rent=rent
        self.food=food
        self.travel=travel
        self.other=other
    def calculate_total_expenses(self):
        self.total=self.rent+self.food+self.travel+self.other
    def calculate_savings(self):
        self.saving=self.salary-self.total
    def display_expense_report(self):
        print(f"""Person name: {self.name}
Monthly Salary: {self.salary}
Rent: {self.rent}
Food: {self.food}
Travel: {self.travel}
Other Expenses: {self.other}
Expected result:
Total Expenses: {self.total}
Savings: {self.saving}""")

t=expensetracker()
a=input("Enter Person Name:")
b=int(input("Enter salary:"))
c=int(input("Enter rent:"))
d=int(input("Enter Food Expense:"))
e=int(input("Enter TRavel Expense:"))
f=int(input("Enter other expenses:"))
t.expense(a,b,c,d,e,f)
t.calculate_total_expenses()
t.calculate_savings()
t.display_expense_report()