#35. Find the first word that is a palindrome.

string=input("Enter string:").split()
for i in range(len(string)):
	rev=string[i][::-1]
	if rev==string[i]:
		print(string[i])
		break