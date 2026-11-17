#53. Remove all punctuation characters.

string=input("Enter String:")
n=''
for i in string:
	if "a"<=i<="z" or "A"<=i<="Z" or "0"<=i<="9" or i==" " and i not in ".,?!:;'""-_()/":
		n=n+i
print(n)