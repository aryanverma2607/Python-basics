#23. Print all characters that occur exactly twice.

string=input("Enter String: ")
vis=''
for i in string:
	if i not in vis:
		vis=vis+i
		c=string.count(i)
		if c==2:
			print(i,end=" ")