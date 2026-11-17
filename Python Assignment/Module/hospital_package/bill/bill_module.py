'''
4. Billing Package

Create a package named "billing".

Create module:
billing_module.py


Implement:


generate_bill()


Take:

- Patient ID
- Consultation Charges
- Medicine Cost
- Test Charges


Calculate total amount:

Total Bill = Consultation Charges + Medicine Cost + Test Charges


Display complete bill.


'''
def generate_bill():
    d={}
    d["p_id"]=input("Enter patient Id:")
    d["c_charge"]=int(input("Enter Consultation Charges:"))
    d["M_charge"]=int(input("Enter medicine Charges:"))
    d["t_charge"]=int(input("Enter test Charges:"))
    
    total=d["c_charge"]+d["M_charge"]+d["t_charge"]

    return total