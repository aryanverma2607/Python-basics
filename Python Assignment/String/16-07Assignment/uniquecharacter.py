'''
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:

```
aabbccdde
```

Output:

```
5
```

'''
string=input("Input :")
visited=''
count=0
for i in range(len(string)):
	ch=string[i]
	if ch not in visited:
		if ch==string[i+1]:
			count=count
		else:
			count=count+1
			visited=visited+ch
print(count)