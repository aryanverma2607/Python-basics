#38. Reverse words without using split().

string=input("Enter string: ")
n=''
for k in range(len(string)-1,-1,-1):
	n=n+string[k]
print(n)