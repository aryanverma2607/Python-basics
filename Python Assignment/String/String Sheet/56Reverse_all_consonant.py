#56. Reverse only consonants in a string.

string=input("Enter string:")
c=''

for i in string:
	if i not in "aeiouAEIOU":
		c=c+i
rev=c[::-1]
k=0
n=''
for j in string:
	if j in "aeiouAEIOU":
		n=n+j
	else:
		while k<len(rev):
			if rev[k] not in "aeiouAEIOU":
				n=n+rev[k]
				k+=1
				break
print(n)