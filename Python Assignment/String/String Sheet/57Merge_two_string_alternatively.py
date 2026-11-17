#57. Merge two strings alternatively (char by char).

#s1-abcd s2-efg o\p s-aebfcgd

s1=input("Enter String1:")
s2=input("Enter String2:")

i=0
j=0
while i<len(s1):
	print(s1[i],end="")
	while j<len(s2):
		print(s2[j],end="")
		j+=1
		break
	i+=1