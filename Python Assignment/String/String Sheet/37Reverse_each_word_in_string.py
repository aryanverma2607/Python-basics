#37. Reverse each word in a string.
#cat dog == tac god
string=input("Enter string: ").split()
new=''
for i in range(len(string)):
	ch=string[i][::-1]
	new=new+" "+ch
print(new.lstrip())