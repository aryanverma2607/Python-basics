#39. Search all occurrences of a character.

string=input("Enter string: ")
s=input("Enter Character: ")

for i in range(len(string)):
	if s==string[i]:
		print(i,end=" ")
