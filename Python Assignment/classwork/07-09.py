'''
def factorial(n):
    if n==0 or n==1:
         return 1
    return n*factorial(n-1)
'''
def power(num,pow):
    if pow==0:
        return 1
    return num*power(num,pow-1)