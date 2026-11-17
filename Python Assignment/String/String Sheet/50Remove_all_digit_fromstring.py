#50. Remove all digits from a string.

string=input("Enter String:")
n=''
for i in string:
	if '0'<=i<='9':
		continue
	else:
		n=n+i
print(n)	