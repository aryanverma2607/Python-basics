print("""========================================
      NUMBER ANALYSIS SYSTEM
========================================""")
def is_perfect(n):
   total=0
   temp=n
   for i in range(1,n):
      if n%i==0:
            total+=i
   if total==temp:
      return "Perfect number"
   else:
      return "Not perfect number"

def is_strong(n):
   total=0
   temp=n
   while n>0:
      r=n%10
      fact=1
      for i in range(1,r+1):
         fact=fact*i
      total=total+fact
      n//=10
   if temp==total:
      return "Strong number"
   else:
      return "Not Strong number"


def pallindrome(n):
   rev=n[::-1]
   if rev==n:
      return "Pallindrome"
   else:
      return "Not Pallindrome"

def is_armstrong(n):
   l=len(str(n))
   sum=0
   temp=n
   while n>0:
      r=n%10
      x=r**l
      sum+=x
      n//=10
   if temp==sum:
      return "Armstrong Number"
   else:
      return "Not Armstrong Number"


import math
def is_prime(n):
   c=0
   for i in range(2,int(math.sqrt(n))+1):
      if n%i==0:
         c+=1
   if c==0:
      return "Prime number"
   else:
      return "Non Prime number"

def evod(n):
   if n%2==0:
      return "Even Number"
   else:
      return "Odd Number"

def factorial(n):
   fact=1
   for i in range(1,n+1):
      fact=fact*i
   return fact

def sum(n):
   sum=0
   while n>0:
      r=n%10
      sum=sum+r
      n//=10
   return sum

def reverse(n):
   rev=0
   while n>0:
      r=n%10
      rev=rev*10+r
      n=n//10
   return rev

def digit(n):
   count=0
   while n>0:
      r=n%10
      if 0<=r	<=9:
         count+=1
      n//=10
   return count

def is_automorphic(n):
   l=len(str(n))
   sq=n*n
   if sq%10**l==n:
      return "Automorphic number"
   else:
      return "Non Automorphic number"

def is_neon(n):
   sq=n**2
   sum=0
   while sq>0:
      r=sq%10
      sum=sum+r
      sq//=10
   if sum==n:
      return "Neon number"
   else:
      return "Not Neon number"

def is_spy(n):
   sum=0
   pro=1
   while n>0:
      r=n%10
      sum=sum+r
      pro=pro*r
      n//=10
   if sum==pro:
      return "Spy number"
   else:
      return "Not Spy number"

def is_harshad(n):
   sum=0
   temp=n
   while n>0:
      r=n%10
      sum=sum+r
      n//=10
   if temp%sum==0:
      return "Harshad Number"
   else:
      return "Not Harshad Number"

while True:
   print("""========================================
   NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit""")
   choice=int(input("Enter Your Choice:"))
   match choice:
         case 1:
            x=int(input("Enter number: "))
            print(is_perfect(x))
         case 2:
            x=input("Enter number: ")
            print(pallindrome(x))
         case 3:
            x=int(input("Enter number: "))
            print(is_strong(x))
         case 4:
            x=int(input("Enter number: "))
            print(is_armstrong(x))
         case 5:
            x=int(input("Enter number: "))
            print(is_prime(x))
         case 6:
            x=int(input("Enter number: "))
            print(evod(x))
         case 7:
            x=int(input("Enter number: "))
            print(factorial(x))
         case 8:
            x=int(input("Enter number: "))
            print(sum(x))
         case 9:
            x=int(input("Enter number: "))
            print(reverse(x))
         case 10:
            x=int(input("Enter number: "))
            print(digit(x))
         case 11:
            x=int(input("Enter number: "))
            print(is_automorphic(x))
         case 12:
            x=int(input("Enter number: "))
            print(is_neon(x))
         case 13:
            x=int(input("Enter number: "))
            print(is_spy(x))
         case 14:
            x=int(input("Enter number: "))
            print(is_harshad(x))
         case 15:
            print("Thank you for using Number Analysis System...!")
            break
         case __:
            print("Invalid choice...!")
            print("Enter choice Between 1 to 15")



