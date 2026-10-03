'''============================================================
QUESTION 2: HOSPITAL PATIENT BILLING SYSTEM
============================================================
Develop a MENU-DRIVEN Hospital Patient Billing System.
The hospital treats different categories of patients:
1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
Every patient must perform common operations such as:
calculate_bill()
calculate_discount()
calculate_final_amount()
generate_bill()
However, the calculation rules are different for each type
of patient.
Therefore, use ABSTRACTION to design the system.
------------------------------------------------------------
ABSTRACT CLASS:
------------------------------------------------------------
Create an abstract class:
Patient
It should contain appropriate abstract methods required for
billing.
Create the following child classes:
1. GeneralPatient
2. EmergencyPatient
3. InsurancePatient
4. CorporatePatient
------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------
========================================
        HOSPITAL MANAGEMENT SYSTEM
========================================
1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit
Enter your choice:
------------------------------------------------------------
OPTION 1: REGISTER PATIENT
------------------------------------------------------------
Input:
Patient ID
Patient Name
Patient Age
Then display:
1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
Enter patient type:
------------------------------------------------------------
GENERAL PATIENT:
------------------------------------------------------------
Consultation Fee : Rs.500
Room Charge       : Rs.1000 per day
Medicine Charge   : Actual amount
Discount          : No discount
Input:
Number of Days
Medicine Charge
------------------------------------------------------------
EMERGENCY PATIENT:
------------------------------------------------------------
Consultation Fee : Rs.1000
Emergency Charge : Rs.500
Room Charge       : Rs.2000 per day
Medicine Charge   : Actual amount
Discount          : No discount
Input:
Number of Days
Medicine Charge
------------------------------------------------------------
INSURANCE PATIENT:
------------------------------------------------------------
Consultation Fee : Rs.800
Room Charge       : Rs.1500 per day
Medicine Charge   : Actual amount
Insurance covers 70% of the total hospital bill.
Patient pays remaining 30%.
Input:
Number of Days
Medicine Charge
------------------------------------------------------------
CORPORATE PATIENT:
------------------------------------------------------------
Consultation Fee : Rs.700
Room Charge       : Rs.1200 per day
Medicine Charge   : Actual amount
Corporate Discount = 20%
Input:
Number of Days
Medicine Charge
------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------
Enter Patient ID: P1025
Enter Patient Name: Rajesh
Enter Patient Age: 42
Select Patient Type:
1. General
2. Emergency
3. Insurance
4. Corporate
Enter choice: 3
Enter Number of Days: 4
Enter Medicine Charge: 3500
------------------------------------------------------------
EXPECTED OUTPUT:
------------------------------------------------------------
========================================
            PATIENT BILL
========================================
Patient ID       : P1025
Patient Name     : Rajesh
Patient Age      : 42
Patient Type     : Insurance
Consultation Fee : Rs.800.00
Room Charges     : Rs.6000.00
Medicine Charges : Rs.3500.00
----------------------------------------
Total Hospital Bill : Rs.10300.00
Insurance Coverage  : 70%
Insurance Amount    : Rs.7210.00
Patient Payable     : Rs.3090.00
Bill Status         : GENERATED
========================================
------------------------------------------------------------
OPTION 2: GENERATE PATIENT BILL
------------------------------------------------------------
Ask:
Enter Patient ID:
If patient exists, generate and display the bill according
to the patient's type.
The calculation must be performed by the appropriate child
class.
------------------------------------------------------------
OPTION 3: VIEW PATIENT BILL
------------------------------------------------------------
Ask:
Enter Patient ID:
Display the complete patient bill.
If patient does not exist:
Patient record not found.
------------------------------------------------------------
OPTION 4:
------------------------------------------------------------
Display:
Thank you for using Hospital Management System.
'''
from abc import ABC,abstractmethod
class Patient(ABC):
    def __init__(self,patient_id,patient_name,patient_age):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age
    @abstractmethod
    def calculate_bill(self):
        pass
    @abstractmethod
    def calculate_discount(self):
        pass
    @abstractmethod
    def calculate_final_amount(self):
        pass
    @abstractmethod
    def generate_bill(self):
        pass

class GeneralPatient(Patient):
    def __init__(self,patient_id,patient_name,patient_age,days,medicine_charge):
        self.medicine_charge = medicine_charge
        self.days = days
        self.room_charge = 1000
        self.type = "General Patient"
        super().__init__(patient_id,patient_name,patient_age)
    def calculate_bill(self):
        self.consultation_fee = 500
        self.room = self.room_charge * self.days
    def calculate_discount(self):
        self.discount = 0
    def calculate_final_amount(self):
        self.total = self.consultation_fee + self.medicine_charge + self.room + self.discount
    def generate_bill(self):
        print(f"""========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : {self.type}

Consultation Fee : Rs.{self.consultation_fee}
Room Charges     : Rs.{self.room}
Medicine Charges : Rs.{self.medicine_charge}

----------------------------------------

Total Hospital Bill : Rs.{self.total}

Discount            : 0%

Patient Payable     : Rs.{self.total}

Bill Status         : GENERATED

========================================
""")

class EmergencyPatient(Patient):
    def __init__(self,patient_id,patient_name,patient_age,days,medicine_charge):
        self.medicine_charge = medicine_charge
        self.days = days
        self.room_charge = 2000
        self.type = "Emergency Patient"
        super().__init__(patient_id,patient_name,patient_age)

    def calculate_bill(self):
        self.consultation_fee = 1000
        self.emergency = 500
        self.room = self.room_charge * self.days
    def calculate_discount(self):
        self.discount = 0
    def calculate_final_amount(self):
        self.total = self.consultation_fee + self.medicine_charge + self.room + self.emergency + self.discount
    def generate_bill(self):
        print(f"""========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : {self.type}

Consultation Fee : Rs.{self.consultation_fee}
Room Charges     : Rs.{self.room}
Medicine Charges : Rs.{self.medicine_charge}

----------------------------------------

Total Hospital Bill : Rs.{self.total}

Discount            : 0%

Patient Payable     : Rs.{self.total}

Bill Status         : GENERATED

========================================""")

class InsurancePatient(Patient):
    def __init__(self,patient_id,patient_name,patient_age,days,medicine_charge):
        self.medicine_charge = medicine_charge
        self.days = days
        self.room_charge = 1500
        self.type = "Insurance Patient"
        super().__init__(patient_id,patient_name,patient_age)
    def calculate_bill(self):
        self.consultation_fee = 800
        self.room = self.room_charge * self.days
        self.total = self.consultation_fee + self.medicine_charge + self.room
    def calculate_discount(self):
        self.discount = self.total * 70/100
    def calculate_final_amount(self):
        self.final_amount = self.total - self.discount
    def generate_bill(self):
        print(f"""========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : {self.type}

Consultation Fee : Rs.{self.consultation_fee}
Room Charges     : Rs.{self.room}
Medicine Charges : Rs.{self.medicine_charge}

----------------------------------------

Total Hospital Bill : Rs.{self.total}

Insurance Coverage  : 70%
Insurance Amount    : Rs.{self.discount}

Patient Payable     : Rs.{self.final_amount}

Bill Status         : GENERATED

========================================""")
        

class CorporatePatient(Patient):
    def __init__(self,patient_id,patient_name,patient_age,days,medicine_charge):
        self.medicine_charge = medicine_charge
        self.days = days
        self.room_charge = 1200
        self.type = "Corporate Patient"
        super().__init__(patient_id,patient_name,patient_age)
    def calculate_bill(self):
        self.consultation_fee = 700
        self.room = self.room_charge * self.days
        self.total = self.consultation_fee + self.medicine_charge + self.room
    def calculate_discount(self):
        self.discount = self.total * 20/100
    def calculate_final_amount(self):
        self.final_amount = self.total - self.discount
    def generate_bill(self):
        print(f"""========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : {self.type}

Consultation Fee : Rs.{self.consultation_fee}
Room Charges     : Rs.{self.room}
Medicine Charges : Rs.{self.medicine_charge}

----------------------------------------

Total Hospital Bill : Rs.{self.total}

Insurance Coverage  : 20%
Insurance Amount    : Rs.{self.discount}

Patient Payable     : Rs.{self.final_amount}

Bill Status         : GENERATED

========================================""")


patient_id = False
print("""========================================
        HOSPITAL MANAGEMENT SYSTEM
========================================""")
while True:
    print("""1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit""")
    choice = input("Enter Your Choice: ")
    match choice:
        case "1":
            print("""\n------------------------------------------------------------
OPTION 1: REGISTER PATIENT
------------------------------------------------------------""")
            patient_id = input("\nEnter Patient ID: ")
            patient_name = input("Enter Patient Name: ")
            patient_age = int(input("Enter Patient Age: "))
            print("""\n1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient""")
            type = input("Enter Patient Type: ")
            if type == "1":
                print("""------------------------------------------------------------
GENERAL PATIENT:
------------------------------------------------------------""")
                days = int(input("Enter Number Of Days: "))
                medicine_charge = int(input("Enter medicine Charge: "))
                obj = GeneralPatient(patient_id,patient_name,patient_age,days,medicine_charge)
                obj.calculate_bill()
                obj.calculate_discount()
                obj.calculate_final_amount()
                obj.generate_bill()

            elif type == "2":
                print("""------------------------------------------------------------
EMERGENCY PATIENT:
------------------------------------------------------------""")
                days = int(input("Enter Number Of Days: "))
                medicine_charge = int(input("Enter medicine Charge: "))
                obj = EmergencyPatient(patient_id,patient_name,patient_age,days,medicine_charge)
                obj.calculate_bill()
                obj.calculate_discount()
                obj.calculate_final_amount()
                obj.generate_bill()

                
            elif type == "3":
                print("""------------------------------------------------------------
INSURANCE PATIENT:
------------------------------------------------------------""")
                days = int(input("Enter Number Of Days: "))
                medicine_charge = int(input("Enter medicine Charge: "))
                obj = InsurancePatient(patient_id,patient_name,patient_age,days,medicine_charge)
                obj.calculate_bill()
                obj.calculate_discount()
                obj.calculate_final_amount()
                obj.generate_bill()

            elif type == "4":
                print("""------------------------------------------------------------
CORPORATE PATIENT:
------------------------------------------------------------""")
                days = int(input("Enter Number Of Days: "))
                medicine_charge = int(input("Enter medicine Charge: "))
                obj = CorporatePatient(patient_id,patient_name,patient_age,days,medicine_charge)
                obj.calculate_bill()
                obj.calculate_discount()
                obj.calculate_final_amount()
                obj.generate_bill()
            else:
                print("Invalid Choice...")
        case "2":
            id = input('Enter Patient ID: ')
            if patient_id == id :
                obj.calculate_bill()
                obj.calculate_discount()
                obj.calculate_final_amount()
                obj.generate_bill()
            else:
                print("Patient Not Found")
        case "3":
            id = input('Enter Patient ID: ')
            if patient_id == id :
                obj.calculate_bill()
                obj.calculate_discount()
                obj.calculate_final_amount()
                obj.generate_bill()
            else:
                print("Patient Not Found")
        case "4":
            print("Thank you for using Hospital Management System.")
            break
        case __:
            print("Invalid Choice\n")