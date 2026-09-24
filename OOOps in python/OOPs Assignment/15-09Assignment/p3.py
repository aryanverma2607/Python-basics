'''Assignment 3: Bank Account Operations
A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

Account number

Account holder name

Balance

Create the following methods:

deposit() – Add an amount to the balance.

withdraw() – Subtract an amount from the balance.

display_account() – Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000
'''
class bank:
    def acc_details(self,acc_no,holder_n,balance):
        self.acc_no=acc_no
        self.holder_n=holder_n
        self.balance=balance
    def deposit(self,n):
        self.deposit=n
    def withdraw(self,x):
        self.withdraw=x
    def display(self):
        print(f"""Account Number: {self.acc_no}
Account Holder: {self.holder_n}
Opening Balance: {self.balance}
Deposit: {self.deposit}
Withdrawal: {self.withdraw}
Final Balance: {self.balance+self.deposit-self.withdraw}""")

b=bank()
x=int(input("Enter amount to deposit:"))
y=int(input("Enter amount to withdraw:"))
b.acc_details("1233456789","Aryan",5000)
b.withdraw(y)
b.deposit(x)
b.display()