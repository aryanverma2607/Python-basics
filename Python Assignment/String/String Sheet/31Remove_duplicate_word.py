#31. Remove duplicate words from a string.

string=input("Enter String :").split()
new=''
for i in range(len(string)):
	ch=string[i]
	if ch not in new:
		new=new+" "+ch
print(new.lstrip())