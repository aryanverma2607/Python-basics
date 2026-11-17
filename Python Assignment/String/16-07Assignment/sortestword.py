'''
4. Program should work for both uppercase and lowercase letters.

 Find the Shortest Word in a Sentence

Telecom SMS Cost Optimization System

A telecom company charges customers based on the length of words used in bulk SMS campaigns.

The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.

Input:

```
Python is very easy to learn
```

Output:

```
is
```
'''
string=input("Input Sentence: ").split()
smallest=9
for s in string:
	if smallest>len(s):
		smallest=len(s)
	else:
		smallest=smallest
#print(smallest)
for i in string:
	if len(i)==smallest:
		print(i)
		break


