'''
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda


'''
string=input("Input = ")
new=""
for i in range(len(string)):
	if i+1<len(string):
		if string[i]==string[i+1]:
			i=i+1
		else:
			new=new+string[i]
if new!="":
	new=new+string[-1]
print(new)