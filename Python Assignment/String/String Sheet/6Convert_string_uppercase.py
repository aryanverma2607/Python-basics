#6. Convert a String to uppercase
string=input("Enter String:")

for i in string:
	if 'a'<=i<='z':
		print(chr(ord(i)-32),end="")
	else:
		print(i,end="")