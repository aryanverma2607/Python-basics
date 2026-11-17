#42. Check if two strings are equal without using equals().

#S1 = "abc", S2 = "abc"

s1=input("Enter string1: ")
s2=input("Enter string2: ")


if len(s1)!=len(s2):
	print("False")
else:
	if s1 in s2:
		print("True")
	else:
		print("False")