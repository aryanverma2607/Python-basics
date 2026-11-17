#33. Find the longest word in a string.

# "find the longest word" o/p longest

string=input("Enter String: ").split()
large=len(string[0])
for i in range(len(string)):
	l=len(string[i])	
	if l>large:
		large=l
for i in range(len(string)):
	l=len(string[i])
	if l==large:
		print(string[i])
		