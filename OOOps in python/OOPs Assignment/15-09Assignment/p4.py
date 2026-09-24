'''Assignment 4: Rectangle Calculator

 A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:

Length

Breadth

Create the following methods:

calculate_area() – Calculate the area.

calculate_perimeter() – Calculate the perimeter.

display_result() – Display length, breadth, area, and perimeter.

Formulas:

Area = Length × Breadth
Perimeter = 2 × (Length + Breadth)

Sample data:

Length: 15
Breadth: 8

'''
class rectangle:
    def input(self,l,b):
        self.lenght=l
        self.bridth=b
    def calculate_area(self):
        self.area=self.lenght*self.bridth
    def calculate_perimeter(self):
        self.perimeter=2*(self.lenght+self.bridth)
    def display(self):
        print(f"""Length: {self.lenght}
Breadth: {self.bridth}
Area: {self.area}
Perimeter: {self.perimeter}""")

r=rectangle()
r.input(40,30)
r.calculate_area()
r.calculate_perimeter()
r.display()