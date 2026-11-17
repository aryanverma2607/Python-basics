'''
5.

Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
 If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number
'''
n=int(input("Enter Number = "))
if n<0:
	print("Not a Automorphic number")
sq=n**2
a=sq%10**(len(str(n)))
print(f"{sq} is Square of {n}")
if a==n:
	print("{} is Automorphic Number".format(n))

