'''
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System

'''















print("""=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================""")
patient={}
n=int(input("Enter number of patient: "))
for i in range(n):
	d={}
	key=int(input("Enter Patient ID: "))
	d["name"]=input("Enter Patient name: ")
	d["age"]=int(input("Enter Patient age: "))
	d["gender"]=input("Enter gender: ")
	d["disease"]=input("Enter Disease: ")
	d["doctor"]=input("Enter Doctor name: ")
	patient[key]=d
print(patient)
while True:
	print("""
1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit""")
	choice=input("Enter your choice: ")
	match choice:
		case '1':
			d={}
			key=int(input("Enter Patient ID: "))
			d["name"]=input("Enter Patient name: ")
			d["age"]=int(input("Enter Patient age: "))
			d["gender"]=input("Enter gender: ")
			d["disease"]=input("Enter Disease: ")
			d["doctor"]=input("Enter Doctor name: ")
			if key not in patient.keys():
				patient[key]=d
				print("\n{}".format(patient))
			else:
				print("\nPatient already Exist")
		case '2':
			if patient=={}:
				print("Add Patient First...!!")
			else:
				search=int(input("enter Patient ID to search: "))
				for k,v in patient.items():
					if k==search:
						print(v)				
						break
				else:	
					print("Patient not found")
		case '3':
			if patient=={}:
				print("Add Patient First...!!")	
			else:
				search=int(input("enter Patient ID: "))
				for k,v in patient.items():
					if k==search:
						d=input("Enter new disease: ")
						patient[k]["disease"]=d
						print("Disease Updated successfully\n")
						print(patient)
						break
						
				else:	
					print("Patient not found")
		case '4':
			if patient=={}:
				print("Add Patient First...!!")
			else:
				search=int(input("enter Patient ID: "))
				for k,v in patient.items():
					if k==search:
						patient.pop(k)
						print("Patient Record Deleted Successfully\n")
						print(patient)
						break
				else:	
					print("Patient not found")
		case '5':
			if patient=={}:
				print("Add Patient First...!!")
			else:
				for k,v in patient.items():
					print("Patient ID	:",k)
					for i,value in v.items():
						print(f"{i}		:{value}")
		case '6':
			if patient=={}:
				print("Add Patient First...!!")
			else:
				print("Total count : {}".format(len(patient)))
		case '7':
			if patient=={}:
				print("Add Patient First...!!")
			else:
				d=input("Enter disease: ")		
				for k,v in patient.items():
					for i,j in v.items():
						if j==d:
							print(k,":",v["name"])
		case '8':
			if patient=={}:
				print("Add Patient First...!!")
			else:
				highest=0		
				for k,v in patient.items():
					for i,j in v.items():
						if v["age"]>highest:
							highest=v["age"]
				for k,v in patient.items():
					if highest==v["age"]:
						print("\nPatient id 	:",k)
						for i,j in v.items():	
							print(i,"		:",j)		
		case '9':
			if patient=={}:
				print("Add Patient First...!!")
			else:		
				lowest=1000
				for k,v in patient.items():
					for i,j in v.items():
						if v["age"]<lowest:
							lowest=v["age"]
				for k,v in patient.items():
					if lowest==v["age"]:
						print("\nPatient id 	:",k)
						for i,j in v.items():	
							print(i,"	:",j)
				
		case '10':
			print("Thank You For Using Hospital Patient Management System")
			break
		case __:
			print("Invalid choice...!")