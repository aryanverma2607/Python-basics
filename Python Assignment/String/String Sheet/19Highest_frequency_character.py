#19. Find the highest frequency character in a string.

string=input("Enter String: ")
vis=''
highest=0
for i in string:
	if i not in vis:
		vis=vis+i
		c=string.count(i)
		if c>highest:
			highest=c
new=''
for i in string:
	if string.count(i)==highest:
		if i not in new:
			print(i,end=" ")
			new=new+i
			

		
			