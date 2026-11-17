'''
5.
Cybercrime Log Analysis System

A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.

If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a
'''
string=input("Input = ")
if string[0]==string[-1]:
	print(string[0])
else:
	print("No repeating character found")