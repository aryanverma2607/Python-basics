#52. Remove all special characters.

string=input("Enter String:")
n=''
for i in string:
	if "a"<=i<="z" or "A"<=i<="Z" or "0"<=i<="9" or i==" ":
		n=n+i
print(n)