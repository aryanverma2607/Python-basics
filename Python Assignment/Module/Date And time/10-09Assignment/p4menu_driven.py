'''
Assignment 4 – Menu-Driven Future Date Calculator

Develop a menu-driven Python program using the datetime module to calculate a future date.

The program should allow the user to add days, weeks, hours, or minutes to a given date/time.

Use timedelta for all date and time calculations.

Menu
========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice:
Case 1 – Add Days

Read:

Starting date
Number of days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to add: 100
Output
Starting Date : 10-09-2026
Days Added    : 100
Future Date   : 19-12-2026
Case 2 – Add Weeks

Read:

Starting date
Number of weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to add: 4
Output
Starting Date : 10-09-2026
Weeks Added   : 4
Future Date   : 08-10-2026
Case 3 – Add Hours

For this case, the student should take date and time as input.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to add: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Added          : 15
Future Date & Time   : 11-09-2026 01:30

This case should test whether students understand that adding hours can change the date.

Case 4 – Add Minutes

Take date/time and number of minutes.

Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 23:30
Enter number of minutes to add: 90
Output
Starting Date & Time : 10-09-2026 23:30
Minutes Added        : 90
Future Date & Time   : 11-09-2026 01:00

Students must correctly handle the change from 10 September → 11 September.

Case 5 – Exit
Enter your choice: 5

Thank you for using Future Date Calculator!

'''
from datetime import date,datetime,timedelta
while True:
    print("""\nMenu
========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit""")
    choice=int(input("Enter Your choice: "))
    match choice:
        case 1:
            dt=input("Enter date (YY-MM-DD):")
            day=int(input("Enter number of days:"))
            date_=datetime.strptime(dt,"%d-%m-%Y")
            formatdate1=datetime.strftime(date_,"%d-%m-%Y")
            new_date=date_+timedelta(days=day)
            formatdate=datetime.strftime(new_date,"%d-%m-%Y")
            print(f"""Starting Date : {formatdate1}
Days Added    : {day}
Future Date   : {formatdate}""")
        case 2:
            dt=input("Enter date (YY-MM-DD):")
            week=int(input("Enter number of weeks:"))
            date_=datetime.strptime(dt,"%d-%m-%Y")
            d=week*7
            new_date=date_+timedelta(days=d)
            formatdate=datetime.strftime(new_date,"%d-%m-%Y")
            print(f"""Starting Date : {dt}
Weeks Added    : {week}
Future Date   : {formatdate}""")
        case 3:
            dt=input("Enter date (YY-MM-DD HH:MM):")
            hour=int(input("Enter Hours:"))
            date_=datetime.strptime(dt,"%d-%m-%Y %H:%M")
            new_date=date_+timedelta(hours=hour)
            formatdate=datetime.strftime(new_date,"%d-%m-%Y %H:%M")
            print(f"""Starting Date & Time : {dt}
Hours Added          : {hour}
Future Date & Time   : {formatdate}""")
        case 4:
            dt=input("Enter date (YY-MM-DD HH:MM):")
            minute=int(input("Enter Minutes:"))
            date_=datetime.strptime(dt,"%d-%m-%Y %H:%M")
            new_date=date_+timedelta(minutes=minute)
            formatdate=datetime.strftime(new_date,"%d-%m-%Y %H:%M")
            print(f"""Starting Date & Time : {dt}
Hours Added          : {minute}
Future Date & Time   : {formatdate}""")
        case 5:
            print("Thank you for using Future Date Calculator!")
            break
        case __:
            print("Inappropriate Choice")