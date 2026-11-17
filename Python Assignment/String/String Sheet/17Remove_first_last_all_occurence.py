#17. Remove the first, last, or all occurrences of a given character.

string=input("Enter String: ")
char=input("Enter Character: ")
s=''
for i in range(len(string)):
	if string[i]==char:
		continue
	else:
		s=s+string[i]
print(s)
