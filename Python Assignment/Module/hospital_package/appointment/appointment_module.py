'''
3. Appointment Management Package

Create a package named "appointment".

Create module:
appointment_module.py


Implement:


a) book_appointment()

Take appointment details:

- Appointment ID
- Patient ID
- Doctor ID
- Appointment Date
- Appointment Time


Store appointment information.


b) show_appointments()

Display all booked appointments.

'''


def book_appointment():
    d={}
    d["ap_id"]=input("Enter appointment Id:")
    d["p_id"]=input("Enter patient Id:")
    d["D_id"]=input("Enter doctor Id:")
    d["date"]=input("Enter appointment date(DD-MM-YYYY):")
    d["time"]=input("Enter appointment time(HH:MM):")
    return d

def show_appointment(n):
    for i in range(len(n)):
        for i,j in n[i].items():
            print(i,":",j)
        print()

