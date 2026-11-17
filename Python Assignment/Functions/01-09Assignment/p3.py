'''
3.
ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System.
 The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements

Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information

* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1

Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---

Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully

---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully

---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000

---

Enter Choice : 5

Customer Profile Displayed Successfully

---

Enter Choice : 6

Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.

Note:
Marks will be awarded based on the correct usage of the specified argument type in each menu option.
'''
def register(name,mail,number):
    print("Customer Name : ",name)
    print("Customer Mail id : ",mail)
    print("Customer Phone Number: ",number)
    print("\nCustomer Registered Successfully")

def product(name,price,category):
    print("Product Name :",name)
    print("Product Price :",price)
    print("Product Category :",category)
    print("\nProduct Details Displayed Successfully")

def invoice(name,price,tax=20):
    taxes=price*0.2
    final_amount=price+taxes
    print("Product Name :",name)
    print("Product Price :",price)
    print("Product Final Price :",final_amount)
    print("\nInvoice generated Successfully...")

def multi(*n):
    return sum(n)

def profile(**x):
   for k,v in x.items():
       print(k,":",v)
   print("Customer profile Displated Successsfully ")
   return x
while True:
   print("""
1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit""")
   choice=input("Enter your choice:") 
   match choice:
        case '1':
            x=input("Enter Cutomer name:")
            y=input("Enter Email-id:")
            while True:
               z=input("Enter phone number:")
               if len(z)!=10:
                  print("Invalid Phone number")
               else:
                  break
            register(x,y,z)
        case '2':
            n=input("Enter Product Name:")
            p=int(input("Enter price of Product:"))
            c=input("Enter Product Category:")
            product(name=n,price=p,category=c)
        case '3':
            n=input("Enter Product Name:")
            p=int(input("Enter price of Product:"))
            invoice(n,p)
        case '4':
            n=int(input("Enter number of product:"))
            product=[]
            for i in range(n):
                x=int(input(f"Enter price of product {i+1}:"))
                product.append(x)
            print("\nTotal Bill Amount :",multi(*product))
        case '5':
            name=input("Enter customer Name : ")
            city=input("Enter city : ")
            y=input("Enter Email-id:")
            while True:
               z=input("Enter phone number:")
               if len(z)!=10:
                  print("Invalid Phone number")
               else:
                  break
            member=input("Enter memebership type:")

            profile(name=name,city=city,email=y,mobile=z,member=member)
        case '6':
            print("Thank you...")
            break






