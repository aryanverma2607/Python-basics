#58. Rotate characters by 2 positions to the left.

#s1=abcde o/p = cdeab

string=input("Enter String:")

a=string[2::]
b=string[:2] 
print(a+b)