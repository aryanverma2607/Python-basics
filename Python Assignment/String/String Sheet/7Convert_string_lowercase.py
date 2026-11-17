#7. Convert a string to lowercase
string=input("Enter String:")

for i in string:
	if 'A'<=i<='Z':
		print(chr(ord(i)+32),end="")
	else:
		print(i,end="")