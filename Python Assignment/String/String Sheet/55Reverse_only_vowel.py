#55. Reverse only vowels in a string.

#hello  holle


string=input("Enter string:")

v=''
for i in string:
	if i in 'AEIUOaeiou':
		v=v+i
rev=v[::-1]
n=''
k=0
for j in string:
	if j not in "aeiouAEIOU":
		n=n+j
	else:
		while k<len(rev):
			n=n+rev[k]
			k+=1
			break
print(n)