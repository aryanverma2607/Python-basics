'''
6. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


a=input("Enter first binary number:")
b=input("Enter Second binary number:")
c=int(a,2)
d=int(b,2)
s=c+d
print(f"Binary Addition of {a} and {b} is {bin(s)[2:]}")