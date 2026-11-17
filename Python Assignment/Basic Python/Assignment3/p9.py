print("Fuel Cost Calculator")
distance,mileage,petrol_price=map(int,input("Enter distance in (Km),mileage(km/l) and petrol price separated by commas:").split(","))
a=distance//mileage
fuel_cost=a*petrol_price
print("Cost of fuel is:{}".format(fuel_cost))