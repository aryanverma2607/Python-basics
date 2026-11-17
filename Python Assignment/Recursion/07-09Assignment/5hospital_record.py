'''
5.
 Hospital Record System (Search Digit)


A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found
'''

def found(n,k):
    if n==0:
      return 0
    if n%10==k:
      return 1
    return found(n//10,k)

x=int(input("Enter Patient ID: "))
k=int(input("Enter digit to found:"))

result=found(x,k)
if result==0:
   print("Not found")
else:
   print("Digit found")
