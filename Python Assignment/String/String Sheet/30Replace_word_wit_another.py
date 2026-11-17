#30. Replace a word with another word.

string=input("Enter string:")
word=input("Enter word to replace:")
new=input("Enter new word to replace:")

print(string.replace(word,new))
words=string.split()
s=''
for i in words:
	if i==word:
		s=s+" "+new
	else:
		s=s+" "+i
print(s.lstrip())