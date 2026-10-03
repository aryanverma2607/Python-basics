'''============================================================
QUESTION 1: ONLINE PAYMENT MANAGEMENT SYSTEM
============================================================
Develop a MENU-DRIVEN Online Payment Management System for an
e-commerce company.
The company supports different payment methods:
1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Every payment method follows a common payment process, but the
actual validation, authentication, processing fee and payment
processing logic are different.

Therefore, the system must be designed using ABSTRACTION.
------------------------------------------------------------
ABSTRACT CLASS:
------------------------------------------------------------

Create an abstract class named:
Payment

The class should define the following abstract methods:
1. validate_payment()
2. calculate_processing_fee()
3. authenticate_payment()
4. process_payment()
5. generate_receipt()

Create separate child classes for:

1. UPIPayment
2. CreditCardPayment
3. DebitCardPayment
4. NetBankingPayment
5. WalletPayment

Each child class must provide its own implementation of all
required abstract methods.

------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------

========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit

Enter your choice:

------------------------------------------------------------
OPTION 1: MAKE PAYMENT
------------------------------------------------------------

Ask the user to enter:

Customer Name
Order ID
Order Amount

Then display:

Select Payment Method

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Enter your choice:

------------------------------------------------------------
UPI:
------------------------------------------------------------

Input:

UPI ID
UPI PIN

Processing Fee:

0%

------------------------------------------------------------
CREDIT CARD:
------------------------------------------------------------

Input:

Card Number
Card Holder Name
CVV
Expiry Date

Processing Fee:

2% of Order Amount

------------------------------------------------------------
DEBIT CARD:
------------------------------------------------------------

Input:

Card Number
Card Holder Name
CVV
Expiry Date

Processing Fee:

1% of Order Amount

------------------------------------------------------------
NET BANKING:
------------------------------------------------------------

Input:

Bank Name
Account Number
Customer ID

Processing Fee:

0.5% of Order Amount

------------------------------------------------------------
WALLET:
------------------------------------------------------------

Input:

Wallet Name
Mobile Number
Wallet PIN

Processing Fee:

1.5% of Order Amount

------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------

Enter Customer Name: Rahul
Enter Order ID: ORD1052
Enter Order Amount: 5000

Select Payment Method:

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Enter your choice: 2

Enter Card Number: 4567891234567890
Enter Card Holder Name: Rahul Singh
Enter CVV: 321
Enter Expiry Date: 12/29

------------------------------------------------------------
EXPECTED OUTPUT:
------------------------------------------------------------

========================================
            PAYMENT PROCESSING
========================================

Customer Name       : Rahul
Order ID            : ORD1052
Payment Method      : Credit Card

Order Amount        : Rs.5000.00
Processing Fee      : Rs.100.00
Final Amount        : Rs.5100.00

Validating payment details...
Payment details validated successfully.

Authenticating payment...
Authentication successful.

Processing payment...
Payment processed successfully.

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================

OPTION 2: VIEW PAYMENT DETAILS
------------------------------------------------------------

Ask:

Enter Order ID:

If the order exists, display:

Order ID
Customer Name
Payment Method
Order Amount
Processing Fee
Final Amount
Transaction ID
Payment Status

If the order does not exist:

Payment record not found.

OPTION 3:

Display:

Thank you for using Online Payment System.
'''
from abc import ABC,abstractmethod
class Payment(ABC):
    def __init__(self,CustomerName,Order_ID,Order_amount):
        self.CustomerName = CustomerName
        self.Order_ID = Order_ID
        self.Order_amount = Order_amount
    @abstractmethod
    def validate_payment(self):
        pass
    @abstractmethod
    def calculate_processing_fee(self):
        pass
    @abstractmethod
    def authentication_payment(self):
        pass
    @abstractmethod
    def process_payment(self):
        pass
    @abstractmethod
    def generate_report(self):
        pass


class UPIPayment(Payment):
    def __init__(self,CustomerName,Order_ID,Order_amount,UPI_id,UPI_Pin):
        self.UPI_id = UPI_id
        self.method = "UPI"
        self.UPI_pin = UPI_Pin
        super().__init__(CustomerName,Order_ID,Order_amount)

    def validate_payment(self):
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.Order_amount * 0/100
        self.total = self.Order_amount + self.processing_fee

    def authentication_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_report(self):
        print(f"""========================================
            PAYMENT PROCESSING
========================================

Customer Name       : {self.CustomerName}
Order ID            : {self.Order_ID}
Payment Method      : {self.method}

Order Amount        : Rs.{self.Order_amount}
Processing Fee      : Rs.{self.processing_fee}
Final Amount        : Rs.{self.total}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authentication_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")

class CreditCardPayment(Payment):
    def __init__(self,CustomerName,Order_ID,Order_amount,card_number,card_holder_name,Cvv,expiry_date):
        super().__init__(CustomerName,Order_ID,Order_amount)
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.Cvv = Cvv
        self.expiry_date=expiry_date
        self.method = "Credit Card"
    def validate_payment(self):
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.Order_amount * 2/100
        self.total = self.Order_amount + self.processing_fee

    def authentication_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_report(self):
        print(f"""========================================
            PAYMENT PROCESSING
========================================

Customer Name       : {self.CustomerName}
Order ID            : {self.Order_ID}
Payment Method      : {self.method}

Order Amount        : Rs.{self.Order_amount}
Processing Fee      : Rs.{self.processing_fee}
Final Amount        : Rs.{self.total}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authentication_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")

class DebitCardPayment(Payment):
    def __init__(self,CustomerName,Order_ID,Order_amount,card_number,card_holder_name,Cvv,expiry_date):
        super().__init__(CustomerName,Order_ID,Order_amount)
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.Cvv = Cvv
        self.method = "Debit Card"
    def validate_payment(self):
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.Order_amount * 1/100
        self.total = self.Order_amount + self.processing_fee

    def authentication_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_report(self):
        print(f"""========================================
            PAYMENT PROCESSING
========================================

Customer Name       : {self.CustomerName}
Order ID            : {self.Order_ID}
Payment Method      : {self.method}

Order Amount        : Rs.{self.Order_amount}
Processing Fee      : Rs.{self.processing_fee}
Final Amount        : Rs.{self.total}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authentication_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")

class NetBankingPayment(Payment):
    def __init__(self,CustomerName,Order_ID,Order_amount,card_number,card_holder_name):
        super().__init__(CustomerName,Order_ID,Order_amount)
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.method = "NetBankingPayment"
    def validate_payment(self):
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.Order_amount * 0.5/100
        self.total = self.Order_amount + self.processing_fee

    def authentication_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_report(self):
        print(f"""========================================
            PAYMENT PROCESSING
========================================

Customer Name       : {self.CustomerName}
Order ID            : {self.Order_ID}
Payment Method      : {self.method}

Order Amount        : Rs.{self.Order_amount}
Processing Fee      : Rs.{self.processing_fee}
Final Amount        : Rs.{self.total}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authentication_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")

class WalletPayment(Payment):
    def __init__(self,CustomerName,Order_ID,Order_amount,card_number,card_holder_name,expiry_date):
        super().__init__(CustomerName,Order_ID,Order_amount)
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.method = "WalletPayment"
    def validate_payment(self):
        return "Payment details validated successfully."

    def calculate_processing_fee(self):
        self.processing_fee = self.Order_amount * 1.5/100
        self.total = self.Order_amount + self.processing_fee

    def authentication_payment(self):
        return "Authentication successful."

    def process_payment(self):
        return "Payment processed successfully."

    def generate_report(self):
        print(f"""========================================
            PAYMENT PROCESSING
========================================

Customer Name       : {self.CustomerName}
Order ID            : {self.Order_ID}
Payment Method      : {self.method}

Order Amount        : Rs.{self.Order_amount}
Processing Fee      : Rs.{self.processing_fee}
Final Amount        : Rs.{self.total}

Validating payment details...
{self.validate_payment()}

Authenticating payment...
{self.authentication_payment()}

Processing payment...
{self.process_payment()}

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")


while True:
    print("""
========================================
        ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit""")
    choice = input("Enter Your Choice:")
    CustomerName=input("\nEnter Customer Name: ")
    Order_ID = input("Enter Order Id: ")
    Order_amount = int(input("Enter Order Amount: "))
    match choice:
        case "1":
            print("""Select Payment Method

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet""")
            choices = input("Payment method: ")
            match choices:
                case "1":
                    print("""------------------------------------------------------------
UPI:
------------------------------------------------------------
""")
                    UPI_id=input("Enter UPI ID: ")
                    UPI_pin=int(input("Enter UPI PIN: "))
                    obj=UPIPayment(CustomerName,Order_ID,Order_amount,UPI_id,UPI_pin)
                    obj.calculate_processing_fee()
                    obj.generate_report()
                case "2":
                    print("""------------------------------------------------------------
CREDIT CARD:
------------------------------------------------------------""")
                    card_number = int(input("Enter Card Number: "))
                    card_holder_name = input("Enter Card Holder Name: ")
                    Cvv = int(input("Enter Card CVV: "))
                    Expiry_date = input("Enter Expiry Date (YYYY/MM/DD): ")
                    obj = CreditCardPayment(CustomerName,Order_ID,Order_amount,card_number,card_holder_name,Cvv,Expiry_date)
                    obj.calculate_processing_fee()
                    obj.generate_report()
                case "3":
                    print("""------------------------------------------------------------
DEDIT CARD:
------------------------------------------------------------""")
                    card_number = int(input("Enter Card Number: "))
                    card_holder_name = input("Enter Card Holder Name: ")
                    Cvv = int(input("Enter Card CVV: "))
                    Expiry_date = input("Enter Expiry Date (YYYY/MM/DD): ")
                    obj = DebitCardPayment(CustomerName,Order_ID,Order_amount,card_number,card_holder_name,Cvv,Expiry_date)
                    obj.calculate_processing_fee()
                    obj.generate_report()
                case "4":
                    print("""------------------------------------------------------------
NET BANKING:
------------------------------------------------------------""")
                    bank_name = input("Enter Bank Name: ")
                    Account_number = int(input("Enter Account Number: "))
                    Customer_ID = int(input("Enter Customer ID: "))
                    obj = NetBankingPayment(CustomerName,Order_ID,Order_amount,bank_name,Account_number,Customer_ID)
                    obj.calculate_processing_fee()
                    obj.generate_report()
                case "5":
                    print("""------------------------------------------------------------
WALLET:
------------------------------------------------------------""")
                    wallet_name = input("Enter Wallet Name: ")
                    Mobile_number = int(input("Enter Mobile Number: "))
                    wallet_pin = int(input("Enter Wallet PIN: "))
                    obj = WalletPayment(CustomerName,Order_ID,Order_amount,wallet_name,Mobile_number,wallet_pin)
                    obj.calculate_processing_fee()
                    obj.generate_report()

                case __:
                    print("Invalid Choice")
        case "2":
            id = input("Enter Order ID to find Record: ")
            if id == Order_ID:
                print("Order ID :",Order_ID)
                print("Customer Name :",CustomerName)
                print("Payment Method :",obj.method)
                print("Order Amount :",Order_amount)
                print("Processing Fee :",obj.processing_fee)
                print("Final Amount :",obj.total)
                print("Transaction ID : TXN785421")
                print("Payment Status : SUCCESS")
            else:
                print("Payment record not found.")
        case "3":
            print("Thank you for using Online Payment System.")
            break
        case __:
            print("Invalid Choice")
