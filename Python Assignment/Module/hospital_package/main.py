
from appointment import book_appointment,show_appointment
from doctor import add_doctor,display_doctors
from patient import add_patient,display_patients,search_patients

from bill import generate_bill
patient1=[]
doctor1=[]
appointment1=[]
while True:
    print("""\nMenu:

========== Hospital Management System ==========

1. Add Patient

2. Display Patients

3. Search Patient

4. Add Doctor

5. Display Doctors

6. Book Appointment

7. Show Appointments

8. Generate Bill

9. Exit
""")
    choice=int(input("Enter choice:"))
    match choice:
        case 1:
            n=int(input("Enter number of patient:"))
            for i in range(n):
                patient1.append(add_patient())
            print("\nPatient added successfully")
        case 2:
            display_patients(patient1)
        case 3:
            search_patients(patient1)
        case 4:
            n=int(input("Enter number of Doctor:"))
            for i in range(n):
                doctor1.append(add_doctor())
            print("\nDoctor added successfully")
        case 5:
            display_doctors(doctor1)
        case 6:
            n=int(input("Enter number of appointent:"))
            for i in range(n):
                appointment1.append(book_appointment())
            print("\nAppointment Booked Successfully")
        case 7:
            show_appointment(appointment1)
        case 8:
            print("Total Bill:",generate_bill())
        case 9:
            print("Exit...!")
            print("Thank you for using Hospital Booking System...")
            break
        case 10:
            print("Invalid Choice...!")
    
