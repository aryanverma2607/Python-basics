#69. Count how many times 'life' appears in a string.


string=input("Enter string:")

'''
print(string.count("life"))
'''

words=string.split()

count=0

for i in words:
	if i=="life":
		count+=1
print(count)