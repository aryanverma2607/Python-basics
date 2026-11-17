#18. Replace the first, last, or all occurrences of a character.
#string.replace('replace char','new char')
string=input("Enter String: ")
char=input("Enter Character to replace: ")
c=input("Enter new character : ")
#Using Method           print(string.replace(char,c))
s=''
for i in string:
	if i==char:
		s=s+c
	else:
		s=s+i
print(s)