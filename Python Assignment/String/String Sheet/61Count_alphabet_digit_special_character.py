#61. Count total alphabets, digits, and special characters.

string=input("Enter String:")

n=0
a=0
s=0

for i in string:
	if i.isdigit():
		n+=1
	elif i.isalpha():
		a+=1
	else:
		s+=1
print("Digit {}\nAlphabet {}\nSpecial Character {}".format(n,a,s))