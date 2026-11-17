'''
Assignment 3 — Date Difference Calculator

Create a program that accepts two dates and displays:

Enter first date: 10-09-2026
Enter second date: 25-12-2026

Display:

Difference in days
Difference in weeks
Difference in hours
Difference in minutes

Example:

Days Difference: 106
Weeks Difference: 15
Hours Difference: 2544
Minutes Difference: 152640

'''
from datetime import date,datetime
date1=input("Enter First Date (YY-MM-DD) :")
date2=input("Enter Second Date (YY-MM-DD) :")

date_1=datetime.strptime(date1,"%d-%m-%Y")
date_2=datetime.strptime(date2,"%d-%m-%Y")

diff=date_2-date_1
print(diff)
print(f"""Days Difference: {diff.days}
Weeks Difference: {diff.days//7}
Hours Difference: {diff.days*24}
Minutes Difference: {diff.days*24*60}""")
