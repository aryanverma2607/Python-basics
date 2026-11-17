'''#Exercise 1
print("Time Converter")
Time_duration=int(input("Enter Total time in Second"))
minute=Time_duration//60
hour=Time_duration//3600
print("Hours:",hour)
print("Minutes:",minute)
print("Second:",Time_duration)
print("Hours:",hour,"Minutes:",minute,"Seconds:",Time_duration)
print("========================================")

#Exercise 2
print("Lifetime Calculator")
Age=int(input("Enter your age in years"))
days=Age*365
hours=Age*365*24
minute=hours*60
print("You've lived approximately:")
print("Days:",days)
print("Hours:",hours)
print("Minute:",minute)
print("========================================")

#Exercise 3
print("Split the Bill")
Friends=int(input("Enter number of Friends"))
Amount=int(input("Enter total bill amount"))
bill=Amount//Friends
print("Total bill=",Amount)
print("Friends=",Friends)
print("Each should pay=",bill)
print("========================================")

#Exercise 4
print("Travel Fare Calculator")
distance=int(input("How many kilometers you travel:"))
print("Distance=",distance)
print("Total fare=",distance*15)
print("========================================")

#Exercise 5
print("Shopping Tax Calculator")
amount=int(input("Enter Amount:"))
tax=amount*0.12
Final_amount=amount+tax
print("Cart = ",amount)
print("Tax = ",tax)
print("Total = ",Final_amount)
print("========================================")

#Exercise 6
print("Smart Coin Machine")
amount=int(input("Enter amount in multiple of 5:"))
division10=amount//10
multiple5=amount-division10*10
change5=multiple5//5
print("output=$10 x ",division10,", 5 x ",change5)

#Exercise 7
print("Temperature Converter")
temperature=int(input("Enter temperature in Celsius:"))
fahrenheit=(temperature*(9/5))+32
print("Celsius=>",temperature)
print("Fahrenheit=>",fahrenheit)
print("========================================")

#Exercise 8(Multiple input in single line )
print("Simple Interest Calculator")
principle,rate,time=map(int,input("Enter Amount and rate and time in year").split())
principle=int(input("Enter principle amount"))
rate=int(input("Enter rate"))
time=int(input("Enter time"))
print("Principle=",principle)
print("Rate=",rate)
print("Time=",time)
Si=(principle*rate*time)//100
print("Simple Interest =",Si)
print("========================================")
'''
