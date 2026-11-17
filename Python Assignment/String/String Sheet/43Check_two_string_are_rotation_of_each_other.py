#43. Check if two strings are rotations of each other.

#S1 = "abcde", S2 = "cdeab"

s1=input("Enter string1: ")
s2=input("Enter string2: ")

print(s2 in s1+s1)