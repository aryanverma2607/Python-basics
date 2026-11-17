#59. Rotate characters by 3 positions to the right.

string=input("Enter String:")
a=''
for i in range(len(string)-1,len(string)-4,-1):
	a=string[i]+a
b=string[:len(string)-3]
print(a+b)