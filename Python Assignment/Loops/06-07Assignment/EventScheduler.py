'''1.Leap Year Event Scheduler – Multi-Year Analysis System

A city event management system schedules special festivals only in leap years.

To plan future events, the system analyzes multiple years instead of just one.

Write a program to:

- Read start year and end year from user
- For every year in the range, check whether it is a Leap Year or Not 
- Apply rules:
    - Divisible by 4 → Leap Year candidate  
    - Divisible by 100 → Not Leap Year  
    - Divisible by 400 → Leap Year  

- If leap year → print year with "Event Scheduled"
- Else → print year with "No Event"

- After checking all years:
    - Count total leap years
    - Print total events scheduled

Input:
2000
2005

Output:
2000 → Event Scheduled
2001 → No Event
2002 → No Event
2003 → No Event
2004 → Event Scheduled
2005 → No Event

Total Leap Years = 2
Total Events Scheduled = 2
'''
start_year=int(input("Enter Starting year = "))
end_year=int(input("Enter End Year = "))
count=0
for i in range(start_year,end_year+1):
	if i%4==0 or i%400==0:
		count=count+1
		print(i,"→Event Scheduled")
	else:
		print(i,"→ No Event Scheduled")
print("Total leap year = ",count)
print("Total Event Scheduled = ",count)
	