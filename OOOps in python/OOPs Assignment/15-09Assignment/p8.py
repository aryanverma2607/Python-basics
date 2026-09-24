'''Assignment 8: Car Mileage Calculator
A car owner wants to calculate the mileage and fuel cost of a journey.
Create a class Car with the following attributes:
Car brand
Car model
Distance travelled in km
Fuel consumed in litres
Petrol price per litre

Create the following methods:
calculate_mileage() – Calculate kilometres per litre.
calculate_fuel_cost() – Calculate total fuel cost.
display_trip_details() – Display car and journey details.

Formulas:
Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price

Sample data:
Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105
'''
class car:
    def details(self):
        self.brand=input("Enter Car Brand Name:")
        self.model=input("Enter Car Model:")
        self.distance=int(input("Enter Distance (In KM):"))
        self.fuel=int(input("Enter fuel consumed (in liters):"))
        self.price=int(input("Enter Price of petrol per litre:"))
    def calculate_mileage(self):
        self.milege=self.distance/self.fuel
    def calculate_fuel_cost(self):
        self.cost=self.fuel*self.price
    def display_trip_details(self):
        print(f"""\nCar Brand: {self.brand}
Car Model: {self.model}
Distance: {self.distance} km
Fuel Consumed: {self.fuel} litres
Petrol Price: {self.price}""")
        print(f"""Milege:{self.milege}
Fuel Cost:{self.cost}""")

c=car()
c.details()
c.calculate_mileage()
c.calculate_fuel_cost()
c.display_trip_details()

