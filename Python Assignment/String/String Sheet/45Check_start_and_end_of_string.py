#45. Check whether a string starts with or ends with another string.

s1=input("Enter string:")
prefix=input("\nEnter prefix of string:")
suffix=input("\nEnter suffix of string:")

print(s1.startswith(prefix) and s1.endswith(suffix))



'''
l=len(prefix)
l1=len(suffix)
for i in s1:
	for j in range(l):
		if i!=prefix[j]:
			break
	else:
		print("Not start with {}".format(prefix))
for i in range(len(s1),l1,-1):
	ch=s1[i]
	for j in range(l1):
		if ch!=prefix[j]:
			break
	else:
		print("Not start with {}".format(suffix))
'''