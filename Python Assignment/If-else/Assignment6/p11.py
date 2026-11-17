'''11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600
'''
distance=int(input("Enter Distance: "))
travel_c=input("Enter Class(SLEEPER/AC): ").lower()
price=0
if distance<=100:
	if travel_c=="sleeper":
		price=100
	elif travel_c=="ac":
		price=200
	else:
		print("Unappropriate Class")
elif distance<=500:
	if travel_c=="sleeper":
		price=300
	elif travel_c=="ac":
		price=600
	else:
		print("Unappropriate Class")
else:
	if travel_c=="sleeper":
		price=500
	elif travel_c=="ac":
		price=1000
	else:
		print("Unappropriate Class")
print(f"Total Fare:₹{price}")

