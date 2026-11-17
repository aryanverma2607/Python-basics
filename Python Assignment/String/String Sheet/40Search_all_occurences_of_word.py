#40. Search all occurrences of a word.

#S = "a b a b", Word='b'
# 2, 6 (start indices)

string=input("Enter string: ")
s=input("Enter Word: ")

for i in range(len(string)):
	if string[i] == s:
		print(i,end="")
		continue
