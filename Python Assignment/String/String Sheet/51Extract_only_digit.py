#51. Extract only digits from a string.

string=input("Enter String:")
n=''
for i in string:
	if '0'<=i<='9':
		n=n+i
print(n)	