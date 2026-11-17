from doctor import add_doctor,display_doctors
from patient import add_patient,display_patients,search_patients
patient1=[]
doctor1=[]
while True:
    print("""Menu:

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
            patient1=add_patient(n)