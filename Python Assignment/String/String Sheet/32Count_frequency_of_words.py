#32. Count the frequency of each word in a string.

string=input("Enter String :").split()
n=''
for i in range(len(string)):
	ch=string[i]
	if ch not in n:
		c=string.count(ch)
		print(string[i],c)
	n=n+ch