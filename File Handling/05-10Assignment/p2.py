'''2. Employee Salary Report
A company stores employee salary information in employees.txt.
Each record contains:
EmployeeID,EmployeeName,Department,Salary
Task
Write a Python program to:
Accept employee details.
Store them in the file.
Read the file.
Display employees whose salary is greater than ₹50,000.
Calculate the average salary.
Sample Input
Enter number of employees: 4
101,Ajay,IT,65000
102,Ravi,HR,45000
103,Priya,IT,72000
104,Amit,Sales,48000
Expected Output
Employees with Salary > 50000
--------------------------------
101  Ajay   IT       65000
103  Priya  IT       72000
Average Salary: 57500.00
'''
f = open("employees.txt","w")
n = int(input("Enter number of employee:"))
i=1
total = 0
while i<=n:
    id = input("Enter Employee ID:")
    name = input ("Enter Employee name:")
    department = input("Enter Employee department:")
    Salary = input("Enter Employee Salary:")
    total = total + int(Salary)
    f.write(id + "," + name + "," + department + "," + Salary + "\n")
    i+=1
f.close()

with open("employees.txt","r") as f1:
    for i in f1:
        data = i.split(",")
        data1 = int(data[3])
        if data1 > 50000:
            print("\n" + " ".join(data))
    print(f"Average Salary: {total/n:.2f}")
