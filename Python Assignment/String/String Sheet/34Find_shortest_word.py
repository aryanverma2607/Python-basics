#34. Find the shortest word in a string.


string = input("Enter String: ").split()
smallest=len(string[0])
for i in range(len(string)):
	l=len(string[i])	
	if l<smallest:
		smallest=l
for i in range(len(string)):
	l=len(string[i])
	if l==smallest:
		print(string[i])