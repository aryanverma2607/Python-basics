'''
4. Airline Ticket Pricing Engine

An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.

If class is economy, then check distance. If distance is greater than 1000, then check booking time. If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.

Input:
Class = economy
Distance = 1200
Booking = early

Output:
Ticket Price = 4000
'''
Class=input("Class(business/economy) = ").lower()
distance=int(input("Distance = "))
time=input("Booking Time (early) = ").lower()

if Class=="business":
	if distance>=1000:
		print("Ticket Price = 8000")
	else:
		print("Ticket Price = 5000")
if Class=="economy":
	if distance>=1000:
		if time=="early":
			print("Ticket Price = 4000")
		else:
			print("Ticket Price = 5000")
	else:
		print("Ticket Price = 2500")
