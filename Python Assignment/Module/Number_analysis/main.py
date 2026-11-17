import math_operation



while True:
    print("""\n========================================
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
            x=int(input("Enter number:"))
            print("\n",math_operation.perfect(x))
        case 2:
            x=input("Enter number:")
            print("\n",math_operation.pallindrome(x))
        case 3:
            x=int(input("Enter number:"))
            print("\n",math_operation.strong(x))
        case 4:
            x=int(input("Enter number:"))
            print("\n",math_operation.armstrong(x))
        case 5:
            x=int(input("Enter number:"))
            print("\n",math_operation.prime(x))
        case 6:
            x=int(input("Enter number:"))
            print("\n",math_operation.evod(x))
        case 7:
            x=int(input("Enter number:"))
            print("\n",math_operation.factorial(x))
        case 8:
            x=int(input("Enter number:"))
            print("\n",math_operation.sum(x))
        case 9:
            x=int(input("Enter number:"))
            print("\n",math_operation.reverse(x))
        case 10:
            x=int(input("Enter number:"))
            print("\n",math_operation.digit(x))
        case 11:
            x=int(input("Enter number:"))
            print("\n",math_operation.automorphic(x))
        case 12:
            x=int(input("Enter number:"))
            print("\n",math_operation.neon(x))
        case 13:
            x=int(input("Enter number:"))
            print("\n",math_operation.spy(x))
        case 14:
            x=int(input("Enter number:"))
            print(math_operation.harshad(x))
        case 15:
            print("Exit...!")
            break
        case __:
            print("Invalid Choice...!")
