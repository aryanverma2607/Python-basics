'''
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
'''
string=input("Input = ")
largest=0
for i in string:
	count=0
	for j in string:
		if i==j:
			count=count+1
		else:
			count=count
	if count>largest:
		largest=count
		print(i,count) 