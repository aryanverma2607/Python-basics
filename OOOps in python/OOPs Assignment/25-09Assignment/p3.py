'''Assignment 3 – Bank Account System

Create a parent class BankAccount with:

account_no
holder_name
balance

Create two child classes:

SavingsAccount
CurrentAccount
Requirements
Take account details from the user.
Use super() to initialize the common attributes.
Create a method calculate_interest() in the parent class.
Override this method in both child classes.
Savings Account gets 5% interest.
Current Account gets 2% interest.
Display the account details and calculated interest.
Sample Input
Enter Account Number: 1001
Enter Holder Name: Amit
Enter Balance: 50000
Enter Account Type: Savings


Expected Output
----- Account Details -----
Account Number : 1001
Holder Name    : Amit
Balance        : 50000
Account Type   : Savings
Interest Rate  : 5%
Interest       : 2500
Amount After Interest : 52500
'''
class Account:
    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def calculate_interest(self):
        return 0

class SavingAccount(Account):
    def __init__(self,account_number,holder_name,balance):
        super().__init__(account_number,holder_name,balance)

    def calculate_interest(self):
        self.rate = 5
        self.interest_rate = self.balance * self.rate/100
        self.total = self.balance + self.interest_rate
        return self.interest_rate

    

class CurrentAccount(Account):
    def __init__(self,account_number,holder_name,balance):
        super().__init__(account_number,holder_name,balance)

    def calculate_interest(self):
        self.rate = 2
        self.interest_rate = self.balance * self.rate/100
        self.total = self.balance + self.interest_rate
        return self.interest_rate

account_number = int(input("Enter Account number: "))
holder_name = input("Enter Account Holder Name: ")
balance = int(input("Enter Account Balance: "))
account_type = input("Enter Account Type: ").lower()

if account_type == "saving":
    account=SavingAccount(account_number,holder_name,balance)
    account.calculate_interest()

    print(f"""----- Account Details -----
Account Number : {account_number}
Holder Name    : {holder_name}
Balance        : {balance}
Account Type   : {account_type}
Interest Rate  : {account.rate}%
Interest       : {account.interest_rate}
Amount After Interest : {account.total}""")
elif account_type == "current":
    account=CurrentAccount(account_number,holder_name,balance)
    account.calculate_interest()

    print(f"""----- Account Details -----
Account Number : {account_number}
Holder Name    : {holder_name}
Balance        : {balance}
Account Type   : {account_type}
Interest Rate  : {account.rate}%
Interest       : {account.interest_rate}
Amount After Interest : {account.total}""")
else:
    print("Invalid Account Type")

