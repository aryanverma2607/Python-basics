'''
2.
NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit

Requirements

Choice 1 – Check Perfect Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return True if the number is Perfect, otherwise False.
* Display an appropriate message based on the returned value.

Choice 2 – Check Prime Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return a message such as "Prime Number" or "Not a Prime Number".
* Display the returned message.

Choice 3 – Find Reverse of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return the reversed number.
* Display the returned value.

Choice 4 – Calculate Factorial

* Accept a number from the user.
* Pass the number to a function.
* The function should return the factorial value.
* Display the returned value.

Choice 5 – Display Factors of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return all factors of the given number.
* Display the returned factors.

Choice 6 – Exit

'''
def perfect(x):
   sum=0
   for i in range(1,x):
       if x%i==0:
          sum+=i
   if x==sum:
       return "Perfect number"
   else:
       return "Not Perfect number"

def prime(a):
   count=0
   i=2
   while i<=a//2:
      if a%i==0:
         count+=1
      i+=1
   if count==0:
       return "Prime number"
   else:
       return "Not Prime number"

def reverse(x):
   rev=0
   while x>0:
      r=x%10
      rev=rev*10+r
      x//=10
   return rev

def factorial(x):
   fact=1
   for i in range(1,x+1):
       fact*=i
   return fact 

def factor(x):
   for i in range(1,x+1):
       if x%i==0:
          print(i)

while True:
    print("""
1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit""")
    choice=input("Enter your choice:")
    match choice:
        case '1':
           y=int(input("Enter a number : "))
           print(perfect(x=y))
        case '2':
           y=int(input("Enter a number : "))
           print(prime(y))
        case '3':
           y=int(input("Enter a number : "))
           print(reverse(y))
        case '4':
           y=int(input("Enter a number : "))
           print(factorial(y))
        case '5':
           y=int(input("Enter a number : "))
           factor(y)
        case '6':
            print("Exit")
            break
        case __:
            print("Invalid Choice ...")
