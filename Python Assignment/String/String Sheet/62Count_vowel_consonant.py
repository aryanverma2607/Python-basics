#62. Count vowels and consonants.

string=input("Enter String:")

v=0
c=0

for i in string:
	if i.isalpha():
		if i in 'AEIOUaeiou':
			v+=1
		else:
			c+=1
print("Vowel {}\nConsonants {}".format(v,c))