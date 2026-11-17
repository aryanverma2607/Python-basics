#20. Find the lowest frequency character in a string.

string=input("Enter String: ")
vis=''
new=''
lowest=string.count(string[0])
for i in range(len(string)):
	if string[i] not in vis:
		vis=vis+string[i]
		count=string.count(string[i])
		if count<lowest:
			lowest=count
for i in range(len(string)):
	if string.count(string[i])==lowest:
		if string[i] not in new:
			new=new+string[i]
			print(string[i],end=" ")
