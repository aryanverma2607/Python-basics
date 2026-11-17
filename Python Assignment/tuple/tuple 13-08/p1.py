'''
1.

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000

'''
from collections import namedtuple
print("""=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================""")

employee=namedtuple("EmployeeDetail",["emp_id", "emp_name","department","salary"])
n=int(input("Enter number of student : "))
l=[]
for i in range(n):
	print(f"Enter Employee {i+1} detail")
	id=int(input("Enter employee id = "))
	name=input("Enter employee name = ")
	department=input("Enter employee department = ")
	salary=float(input("Enter employee salary = "))	
	e1=employee(id,name,department,salary)
	l.append(e1)
print()
for i in l:
	print(i.emp_id,i.emp_name,i.department,i.salary)
print()
dep=input("Enter department : ")
highest=e1.salary
lowest=e1.salary
sum=0
print()
for i in l:
	sum=sum+i.salary
	if highest<i.salary:
		highest=i.salary
	if lowest>i.salary:
		lowest=i.salary

for i in l:
	if i.salary==lowest:
		print("Lowest Salary Employee")
		print(i.emp_id,i.emp_name,i.department,i.salary)
		print()
	if i.salary==highest:
		print("Highest Salary Employee")
		print(i.emp_id,i.emp_name,i.department,i.salary)
print()
print(F"Average Salary : {sum//n}")
print()
print("Employees in {} Department".format(dep))
for i in l:
	if dep==i.department:
		print(i.emp_id,i.emp_name,i.department,i.salary)
	else:
		print("No such department found")
	