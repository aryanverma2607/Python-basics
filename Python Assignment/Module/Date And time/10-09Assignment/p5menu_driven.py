'''
ASSIGNMENT 5 – MENU-DRIVEN PAST DATE & TIME CALCULATOR


Create a menu-driven Python program that allows the user to calculate a date/time in the past by subtracting days, weeks, hours, or minutes.

Menu
========== PAST DATE & TIME CALCULATOR ==========

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit

Enter your choice:
CASE 1 – Subtract Days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to subtract: 100
Output
Starting Date : 10-09-2026
Days Subtracted : 100
Past Date : 02-06-2026
CASE 2 – Subtract Weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to subtract: 6
Output
Starting Date : 10-09-2026
Weeks Subtracted : 6
Past Date : 30-07-2026
CASE 3 – Subtract Hours

Here the student must read both date and time.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to subtract: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Subtracted     : 15
Past Date & Time     : 09-09-2026 19:30
CASE 4 – Subtract Minutes
Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 01:00
Enter number of minutes to subtract: 90
Output
Starting Date & Time : 10-09-2026 01:00
Minutes Subtracted   : 90
Past Date & Time     : 09-09-2026 23:30
CASE 5 – Exit
Enter your choice: 5

Thank you for using Past Date & Time Calculator!

'''
from datetime import date,datetime,timedelta
while True:
    print("""\nMenu
========== PAST DATE & TIME CALCULATOR ==========

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit""")
    choice=int(input("Enter Your choice: "))
    match choice:
        case 1:
            dt=input("Enter Starting date (YY-MM-DD):")
            day=int(input("Enter number of days to substract:"))
            date_=datetime.strptime(dt,"%d-%m-%Y")
            new_date=date_-timedelta(days=day)
            formatdate=datetime.strftime(new_date,"%d-%m-%Y")
            print(f"""Starting Date : {dt}
Days Added    : {day}
Future Date   : {formatdate}""")
        case 2:
            dt=input("Enter date (YY-MM-DD):")
            week=int(input("Enter number of weeks to substract:"))
            date_=datetime.strptime(dt,"%d-%m-%Y")
            d=week*7
            new_date=date_-timedelta(days=d)
            formatdate=datetime.strftime(new_date,"%d-%m-%Y")
            print(f"""Starting Date : {dt}
Weeks Added    : {week}
Future Date   : {formatdate}""")
        case 3:
            dt=input("Enter date (YY-MM-DD HH:MM):")
            hour=int(input("Enter Hours to substract:"))
            date_=datetime.strptime(dt,"%d-%m-%Y %H:%M")
            new_date=date_-timedelta(hours=hour)
            formatdate=datetime.strftime(new_date,"%d-%m-%Y %H:%M")
            print(f"""Starting Date & Time : {dt}
Hours Added          : {hour}
Future Date & Time   : {formatdate}""")
        case 4:
            dt=input("Enter date (YY-MM-DD HH:MM):")
            minute=int(input("Enter Minutes to substract:"))
            date_=datetime.strptime(dt,"%d-%m-%Y %H:%M")
            new_date=date_-timedelta(minutes=minute)
            formatdate=datetime.strftime(new_date,"%d-%m-%Y %H:%M")
            print(f"""Starting Date & Time : {dt}
Hours Added          : {minute}
Future Date & Time   : {formatdate}""")
        case 5:
            print("Thank you for using Future Date Calculator!")
            break
        case __:
            print("Inappropriate Choice")