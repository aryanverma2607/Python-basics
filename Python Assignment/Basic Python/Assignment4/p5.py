print("Salary Breakdown")
salary,day,hour=map(int,input("Enter your salary and working days and working Hour =").split())
per_day=salary/day
per_hour=per_day/hour
print("input:")
print("Monthly Salary=",salary)
print("Working days=",day)
print("Working Hours per day=",hour)
print("Salary per Day=",per_day)
print("Salary per Hour=",per_hour)