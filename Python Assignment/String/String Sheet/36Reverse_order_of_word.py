#36. Reverse the order of words in a string.

string=input("Enter string:").split()

new=''
for i in range(len(string)-1,-1,-1):
	new=new+" "+string[i]
print(new.lstrip())