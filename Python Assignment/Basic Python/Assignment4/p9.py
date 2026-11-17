print("Petrol Cost Calculator")
distance,mileage,petrol_price=map(int,input("Enter distance in (Km),mileage(km/l) and petrol price separated by commas:").split(","))
a=distance/mileage
fuel_cost=a*petrol_price
print(F"Petrol used = {a}Liters")
print("Total Cost = {}".format(fuel_cost))