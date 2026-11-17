#16. Count total occurrences of a character in a string.

string=input("Enter String: ")
char=input("Enter Character: ")

#print(string.count(char))
count=0
for i in range(len(string)):
	if string[i]==char:
		count+=1
print(count)