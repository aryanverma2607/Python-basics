print("Time Duration Adder")
hour,minute,second=map(int,input("Enter hours,minutes,seconds separated by ':'=").split(":"))
hours=hour*3600
minutes=minute*60
Total_seconds=hours+minutes+second
print("Total Seconds={}".format(Total_seconds))