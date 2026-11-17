#63. Count frequency of each character.

string=input("Enter string:")

n=''
for i in string:
	if i not in n:
		print(string.count(i))
		n=n+i