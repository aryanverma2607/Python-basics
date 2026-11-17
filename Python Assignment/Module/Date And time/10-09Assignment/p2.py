'''
2.
Employee Joining & Experience System

Create an employee experience calculator.

Read:

Employee name
Joining date
Current date

Calculate:

Total days worked
Total years worked
Total months approximately
Experience in Years Months Days
Whether employee has completed 1 year
Whether employee has completed 5 years

Example:

Enter employee name: Rahul
Enter joining date: 10-06-2021
Enter current date: 10-09-2026

Output:

Employee: Rahul
Joining Date: 10-06-2021
Experience: 5 Years 3 Months 0 Days
Total Days Worked: 1918
5 Years Completed: Yes

'''

from datetime import date,datetime,timedelta
ename=input("Enter Employee name:")
join=input("Enter joining date(YY-MM-DD):")
joined_date=datetime.strptime(join,"%d-%m-%Y")
current=datetime.now()
'''#print(current)'''
#print(joined_date)
worked=current-joined_date
print(f"\nEmplyee Name {ename}")
print(f"\nJoined date {joined_date.date()}")
print(f"\nExperience {current.year-joined_date.year} Years {current.month-joined_date.month} Months {current.day-joined_date.day} Days")
print(f"\nTotal Working days {worked.days}")

if current.year-joined_date.year>=5:
    print("\nMore than 5 year completed")
else:
    if current.year-joined_date.year>=1:
        print("\nMore than 1 year completed")
