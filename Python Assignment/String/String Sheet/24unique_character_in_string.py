#24. Check if all characters in a string are unique (no repetition).

string=input("Enter String :")
for i in string:
	if string.count(i)==1:
		continue
	else:
		print("Not all character are unique")
		break
else:
	print("All unique Character")