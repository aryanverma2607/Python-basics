#29. Remove the first, last, or all occurrences of a word.

string=input("Enter string:").split()
word=input("Enter word:")


for i in range(len(string)):
	ch=string[i]
	print(ch)
	if ch in word:
		s=s
	else:
		s=s+" "+ch
print(s.lstrip())