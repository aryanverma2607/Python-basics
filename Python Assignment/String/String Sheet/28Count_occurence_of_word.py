#28. Count occurrences of a word in a string.

string=input("Enter string:").split()
word=input("Enter word:")
count=0
for i in range(len(string)):
	if string[i]==word:
		count+=1
	else:
		continue
print(count)