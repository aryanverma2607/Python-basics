'''
=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2

'''
from collections import namedtuple
print("""=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================""")


hospital=namedtuple("HospitalDetail",["patient_id","patient_name","age","disease"])
n=int(input("Enter number of Patient : "))
l1=[]
for i in range(n):
	print(f"Enter patient {i+1} detail")
	id=input("Enter Patient ID = ")
	name=input("Enter Patient name = ")
	age=int(input("Enter Patient age = "))
	disease=input("Enter Patient disease = ")	
	p=hospital(id,name,age,disease)
	l1.append(p)
print()
for i in l1:
	print(i.patient_id,i.patient_name,i.age,i.disease)
print()
for i in l1:
	if i.age>60:
		print(i.patient_id,i.patient_name,i.age,i.disease)
	else:
		print("No patient age is above 60")
print()
p_id=input("Enter Patient Id = ")
print()
for i in l1:
	if i.patient_id==p_id:
		print(i.patient_id,i.patient_name,i.age,i.disease)
	else:
		print("Patient not found")
print()
d=input("Enter disease = ")
count=0
print()
for i in l1:
	if d==i.disease:
		count+=1
print("Patients with {}:{}".format(d,count))
