#22. Find the last repeating character.
#abracadabra
string=input("Enter String: ")

vis=''
for i in string:
	if i not in vis:
		vis=i+vis
		c=string.count(i)
for j in vis:
	if string.count(j)>1:
		print(j)
		break
else:
	print("All unique")
		