'''
6.
 Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number
'''
import math
def prime(n,k=2):
   if n<2:
      return "not prime"
   if k>(math.sqrt(n)):
      return "Prime"
   if n%k==0:
      return "Not Prime"
   return prime(n,k+1)


x=int(input("Enter Coupon Number: "))
result=prime(x)
print(result)