#68. Count the sum of digits present in a string.

string=input("Enter string: ")
sum=0
for i in range(len(string)):
	if "1"<=string[i]<="9":
		sum+=int(string[i])
print(sum)