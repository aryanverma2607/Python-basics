'''============================================================
ASSIGNMENT 4 – BANK ACCOUNT SYSTEM
==================================

Create an Account class inside:

models/account.py

ATTRIBUTES:

* account_no
* customer_name
* balance

METHODS:

* deposit()
* withdraw()
* display()

TASKS:

1. Create 5 Account objects.
2. Store all Account objects in a list.
3. Display all accounts.
4. Search an account using Account Number.
5. Deposit money into a selected account.
6. Withdraw money from a selected account.
7. Display accounts having balance greater than 50,000.
8. Find the account having the highest balance.

SAMPLE DATA:

101 Amit 45000
102 Rahul 75000
103 Priya 35000
104 Neha 90000
105 Rohit 55000

SAMPLE OPERATIONS:

Enter Account No: 101

Enter amount to deposit: 10000

After Deposit:
101 Amit 55000

Enter Account No: 103

Enter amount to withdraw: 5000

After Withdrawal:
103 Priya 30000

EXPECTED OUTPUT:

Accounts having balance greater than 50000:

102 Rahul 75000
104 Neha 90000
105 Rohit 55000

Highest Balance Account:

104 Neha 90000
'''
details=[]
class account:
    def __init__(self):
        self.acc_no=int(input('Enter Account Number:'))
        self.name=input("Enter Customer Name:")
        self.balance=int(input("Enter Account Balance:"))
        details.append(self)

    def display(self):
        print()
        for i in details:
            print(i.acc_no,i.name,i.balance)

    def found(self):
        self.no=int(input("\nEnter Account Number to found:"))
        for i in details:
            if i.acc_no==self.no:
                print(i.acc_no,i.name,i.balance)
                break
        else:
            print("Account Not found")

    def select_deposit(self):
        self.no=int(input("\nEnter Account Number to deposit:"))
        for i in details:
            if i.acc_no==self.no:
                self.d=int(input("Enter Amount to deposit:"))
                i.balance=i.balance + self.d
                print("\nAccount Balance After Deposit:",i.acc_no,i.name,i.balance)
                break
        else:
            print("Account Not found")

    def select_withdraw(self):
        self.no=int(input("\nEnter Account Number to found:"))
        for i in details:
            if i.acc_no==self.no:
                self.w=int(input("Enter Amount to withdraw:"))
                i.balance=i.balance - self.w
                print("\nAccount Balance After Withdraw:",i.acc_no,i.name,i.balance)
                break
        else:
            print("Account Not found")

    def greater(self):
        print("\nAccounts having balance greater than 50000:")
        for i in details:
            if i.balance>50000:
                print(i.acc_no,i.name,i.balance)

    def highest(self):
        high=0
        for i in details:
            if i.balance>high:
                high=i.balance
        for i in details:
            if i.balance==high:
                print("\nHighest Account Balance:",i.acc_no,i.name,i.balance)

