'''

1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc

'''
string=input("Input = ")
new=""
for i in range(len(string)):
	if i+1<len(string):
		if string[i]==string[i+1]:
			i=i+1
		else:
			new=new+string[i]
new1=""
for j in range(len(new)):
	if j+1<len(new):
		if new[j]==new[j+1]: 	
			continue
		else:
			new1=new1+new[j]
print(new1)
			