#WAP to find all the year between two entered years
x=int(input("Enter Starting year = "))
y=int(input("Enter Ending year = "))
if x<1:
	print("Invalid Entry...!")
else:
	for i in range(x,y+1):
		if i%4==0 or i%100==0 and i%400!=0:
			print(f"{i} is a leap year")
		elif i%4==0:
			print(f"{i} is a leap year")
		else:
			print(f"{i} is not a leap year")
		
