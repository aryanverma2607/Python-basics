#14. Find the first occurrence of a character in a string.

string=input("Enter String: ")
char=input("Enter Character: ")
for i in range(len(string)):
	if string[i]==char:
		print(i)
		break
else:
	print("No such character found")

print(string.find(char))
		