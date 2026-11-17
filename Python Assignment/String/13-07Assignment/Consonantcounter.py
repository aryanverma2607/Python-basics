'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U

'''
s=input("Enter Student name = ").lower()
i=0
count=0
while i<len(s):
	ch=s[i]
	if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
		count=count
	elif ch==" ":
		count=count
	elif ch>="0" and ch<="9":
		count=count
	else:
		count=count+1
	i=i+1
print(f"Total Number of Consonant : {count}")


