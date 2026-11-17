'''
Assignment 1 — Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days
'''

from datetime import date,datetime,timedelta
bdate=input("Enter DOB date(YY-MM-DD):")
new_date=datetime.strptime(bdate,"%d-%m-%Y")
#print(new_date)
today=datetime.now()
#print(date.today())
age=today.year-new_date.year
print("Age:",age)
total_days=today-new_date
print("Total Days Lived:",total_days.days)

d=new_date.day
m=new_date.month
y=today.year
birthday=date(y,m,d)
'''#print(birthday)'''
#print(date.today())
if birthday > date.today():
    print("Next Birthday",birthday)
    days_remain=birthday-date.today()
    print("Days Remained:",days_remain.days)
else:
    a=birthday+timedelta(days=365)
    print("Next Birthday:",a)
    days_remain=a-date.today()
    print("Days Remained:",days_remain.days)



