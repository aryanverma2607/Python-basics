#48. Remove all vowels from a string.

s1=input("Enter string:")

n=''
for i in range(len(s1)):
	if s1[i] in 'aeiouAEIOU':
		continue
	else:
		n=n+s1[i]
print(n)