#54. Replace all duplicate characters with '$'.

string=input("Enter String:")

n=''

for i in string:
	c=string.count(i)
	if c>1:
		n=n+'$'
	else:
		n=n+i
print(n) 