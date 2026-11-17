#21. Find the first non-repeating character.
string=input("Enter String: ")
for i in string:
	c=string.count(i)
	if c==1:
		print(i)
		break
else:
	print("No non-repeating character found")