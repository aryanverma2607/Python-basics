#27. Find the last occurrence of a word in a string.


string=input("Enter string: ")
s=input("Enter Word: ")

for i in range(len(string)):
	if string[i] == s:
		continue
else:
	print(i)
			