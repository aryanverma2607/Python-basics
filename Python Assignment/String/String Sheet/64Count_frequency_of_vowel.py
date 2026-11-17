#64. Count frequency of each vowel.



string=input("Enter string:")
n=''
for i in string:
	if i not in n:
		if i in "AEIOUaeiou":
			print("Vowel {} count {}".format(i,string.count(i)))
			n=n+i