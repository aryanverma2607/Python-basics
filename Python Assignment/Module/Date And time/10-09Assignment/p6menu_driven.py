'''
ASSIGNMENT 6 – EMPLOYEE WORKING DATE & DEADLINE CALCULATOR

You are developing a small HR/Project Management utility.

The HR department wants to calculate important dates related to an employee or project.

Create a menu-driven program that provides the following operations:

========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit

Enter your choice:
CASE 1 – Calculate Probation End Date

An employee joins an organization on a particular date.

The company has a probation period of a specified number of months/days.

For this assignment, take probation period in days.

Input
Enter your choice: 1

Enter employee joining date (DD-MM-YYYY): 15-07-2026
Enter probation period in days: 90
Output
Joining Date       : 15-07-2026
Probation Period   : 90 days
Probation End Date : 13-10-2026

Students should use:

timedelta(days=...)
CASE 2 – Calculate Project Deadline

A software company starts a project on a particular date.

The project manager gives a deadline in terms of number of days.

Calculate the final deadline.

Input
Enter your choice: 2

Enter project start date (DD-MM-YYYY): 10-09-2026
Enter project duration in days: 120
Output
Project Start Date : 10-09-2026
Project Duration   : 120 days
Project Deadline   : 08-01-2027
Important

The program must correctly handle:

Month changes
Year changes
Leap years

Students should not manually calculate these.

CASE 3 – Calculate Notice Period End Date

An employee resigns from a company.

The employee's notice period is given in days.

Calculate the date on which the notice period ends.

Input
Enter your choice: 3

Enter resignation date (DD-MM-YYYY): 20-09-2026
Enter notice period in days: 60
Output
Resignation Date : 20-09-2026
Notice Period    : 60 days
Last Working Date: 19-11-2026
Additional Test

Students should test:

Resignation Date : 15-12-2026
Notice Period    : 60 days

The program must correctly move into 2027.

CASE 4 – Calculate Days Remaining for Deadline

A project has a deadline.

The program should take:

Current date
Project deadline

and calculate how many days are remaining.

Input
Enter your choice: 4

Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 25-09-2026
Output
Current Date     : 10-09-2026
Project Deadline : 25-09-2026
Days Remaining   : 15 days
If deadline has already passed

Input:

Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 01-09-2026

Output:

Current Date     : 10-09-2026
Project Deadline : 01-09-2026
Deadline Status  : Deadline has already passed
Days Overdue     : 9 days
CASE 5 – Check Employee Work Anniversary

The HR department wants to check whether an employee's work anniversary is today.

Take:

Employee joining date
Current date
Input
Enter your choice: 5

Enter employee joining date (DD-MM-YYYY): 10-09-2020
Enter current date (DD-MM-YYYY): 10-09-2026
Output
Joining Date : 10-09-2020
Current Date : 10-09-2026

Work Anniversary: YES
Completed Years  : 6 years
If anniversary is not today

Input:

Enter your choice: 5

Enter employee joining date (DD-MM-YYYY): 15-05-2022
Enter current date (DD-MM-YYYY): 10-09-2026

Output:

Joining Date : 15-05-2022
Current Date : 10-09-2026

Work Anniversary: NO
Completed Years  : 4 years
CASE 6 – Exit
Enter your choice: 6

Thank you for using Employee & Project Date Calculator!
'''
from datetime import date,timedelta,datetime
while True:
    print("""========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit""")
    choice=int(input("Enter Your choice: "))
    match choice:
        case 1:
            dt=input("Enter Date (DD-MM-YYYY): ")
            day=int(input("Enter prbation period in days: "))
            date_1=datetime.strptime(dt,"%d-%m-%Y")
            new_date=date_1+timedelta(days=day)
            fmtdate=datetime.strftime(new_date,"%d-%m-%Y")
            print(f'''Joining Date       : {date_1.date()}
Probation Period   : {day} days
Probation End Date : {fmtdate}''')
        case 2:
            dt=input("Enter Date (DD-MM-YYYY): ")
            day=int(input("Enter prbation period in days: "))
            date_1=datetime.strptime(dt,"%d-%m-%Y")
            new_date=date_1+timedelta(days=day)
            fmtdate=datetime.strftime(new_date,"%d-%m-%Y")
            print(f"""Project Start Date : {date_1.date()}
Project Duration   : {day} days
Project Deadline   : {fmtdate}""")
        case 3:
            dt=input("Enter Resignation Date (DD-MM-YYYY): ")
            day=int(input("Enter Notice period in days: "))
            date_1=datetime.strptime(dt,"%d-%m-%Y")
            new_date=date_1+timedelta(days=day)
            fmtdate=datetime.strftime(new_date,"%d-%m-%Y")
            print(f"""Resignation Date : {date_1.date()}
Notice Period   : {day} days
Last Working Date   : {fmtdate}""")
        case 4:
            date1=datetime.now()
            date2=input("Enter deadline Date:")
            date_1=date1.date()
            date_2=datetime.strptime(date2,"%d-%m-%Y")
            if (date_1-date_2.date()).days<=0:
                print(f"""Current Date     : {date_1}
Project Deadline : {date_2.date()}
Days Remaining   : {(abs(date_1-date_2.date())).days} days
If deadline has already passed""")
            else:
                print(f"""Current Date     : {date_1}
Project Deadline : {date_2.date()}
Deadline Status  : Deadline has already passed
Days Overdue     : {(abs(date_1-date_2.date())).days} days""")
        case 5:
            join=input("Enter joining date: ")
            current=datetime.now()
            j_dt=datetime.strptime(join,"%d-%m-%Y")
            c_dt=current.date()
            j_dt_=j_dt.date()
            if c_dt.day==j_dt_.day and c_dt.month==j_dt_.month:
                print(f"""Work Anniversary: YES
Completed Years  : {c_dt.year-j_dt_.year} years""")
            else:
                print(f"""Joining Date : {j_dt_}
Current Date : {c_dt}
Work Anniversary: NO
Completed Years  : {c_dt.year-j_dt_.year} years""")
        case 6:
            print("Thank you for using Employee & Project Date Calculator!")
            break
        case __:
            print("Inappropriate choice...")
                
