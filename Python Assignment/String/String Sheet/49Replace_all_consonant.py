#49. Replace all consonants with '*'.

string=input("Enter String:")

n=''
for i in string:
	if 'A'<=i<='Z' or 'a'<=i<='z' and i not in 'aeiouAEIOU':
		n=n+'*'
	else:
		n=n+i
print(n) 
		