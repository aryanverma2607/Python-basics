'''Q3. DRIVING LICENSE REGISTRATION
Scenario:
A government driving license registration system needs to validate whether
a person is eligible to apply for a driving license.
Create the following custom exceptions:
1. InvalidAgeForDrivingLicenseException
2. InvalidMarkForDrivingLicenseException
## Eligibility Rules:
1. Age must be greater than or equal to 18.
2. Age cannot be negative.
3. Road rules test marks must be between 0 and 100.
4. A person must score more than 80 marks to pass the test.
## Requirements:
1. Create the Person class with the following attributes:
   name
   age
   mark
2. Create the two custom exception classes.
3. Create a method named check_eligibility().
4. Validate age first.
5. If age is negative, raise:
   InvalidAgeForDrivingLicenseException: Invalid age
6. If age is less than 18, raise:
   InvalidAgeForDrivingLicenseException:
   Age should be more than 18 years old
7. Validate marks.
8. If marks are negative or greater than 100, raise:
   InvalidMarkForDrivingLicenseException: Invalid mark
9. If marks are 80 or less, raise:
   InvalidMarkForDrivingLicenseException:
   Mark should be more than 80
10. If all conditions are satisfied, display:
   Approved
11. Handle all exceptions using try-except.
## Sample Input 1:
Guru
33
95
## Sample Output 1:
Approved
## Sample Input 2:
Smith
17
95
## Sample Output 2:
InvalidAgeForDrivingLicenseException: Age should be more than 18 years old
## Sample Input 3:
Jack
-3
95
## Sample Output 3:
InvalidAgeForDrivingLicenseException: Invalid age
## Sample Input 4:
Scott
33
75
## Sample Output 4:
InvalidMarkForDrivingLicenseException: Mark should be more than 80
## Sample Input 5:
Mathew
33
-45
## Sample Output 5:
InvalidMarkForDrivingLicenseException: Invalid mark
## Sample Input 6:
Guru
33
195
## Sample Output 6:
InvalidMarkForDrivingLicenseException: Invalid mark
'''
class InvalidAgeForDrivingLicenseException(Exception):
   pass
class InvalidMarkForDrivingLicenseException(Exception):
   pass

class Person :
   def __init__(self,name,age,mark):
      self.name = name
      self.age = age
      self.marks = mark
   def check_eligibility(self):
      def age():
         if self.age < 0:
            raise InvalidAgeForDrivingLicenseException("Invalid age")
         elif self.age < 18:
            raise InvalidAgeForDrivingLicenseException("Age should be more than 18 years old")
      age()
      def marks():
         if self.marks < 0 or self.marks >100:
            raise InvalidMarkForDrivingLicenseException("Invalid mark")
         elif self.marks <= 80:
            raise InvalidMarkForDrivingLicenseException("Mark should be more than 80")
      marks()

name = input ("Enter Name :")
age = int(input ("Enter Your Age :"))
marks = int(input ("Enter Your Marks :"))
P = Person(name,age,marks)
try :
   P.check_eligibility()
except InvalidAgeForDrivingLicenseException as e:
   print("InvalidAgeForDrivingLicenseException : ",e)
except InvalidMarkForDrivingLicenseException as e:
   print("InvalidMarkForDrivingLicenseException : ",e)
else:
   print("Approved")